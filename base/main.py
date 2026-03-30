from fastapi import FastAPI, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import json
import asyncio
import time
from tinvest import Task, Worker, utils
from .db_models import Share, TrackedShare, Tile
from .db_worker import DBWorker
from contextlib import asynccontextmanager





load_dotenv()

class AppState:
    def __init__(self):
        self.worker: Worker | None = None
        self.db_worker: DBWorker | None = None
        self.bkg_get_orderbooks = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    state = AppState()

    state.worker = Worker(
        token=os.getenv('TOKEN'),
        url=os.getenv('SANDBOX_URL')
    )
    
    state.db_worker = DBWorker(
        db_user=os.getenv('DB_USER'),
        db_pass=os.getenv('DB_PASSWORD'),
        db_host=os.getenv('DB_HOST'),
        db_port=os.getenv('DB_PORT'),
        db_name=os.getenv('DB_NAME')
    )


    # TODO Фоновая задача !!!
    state.bkg_get_orderbooks = asyncio.create_task(
        get_orderbooks(state.worker, state.db_worker)
    )


    app.state = state

    yield

    # TODO Отмена фоновой задачи
    if state.bkg_get_orderbooks:
        state.bkg_get_orderbooks.cancel()




app = FastAPI(lifespan=lifespan)



async def get_worker() -> Worker:
    if not hasattr(app.state, 'worker') or app.state.worker is None:
        raise RuntimeError("Worker not initialized")
    return app.state.worker

async def get_db_worker() -> DBWorker:
    if not hasattr(app.state, 'db_worker') or app.state.db_worker is None:
        raise RuntimeError("DB Worker not initialized")
    return app.state.db_worker




allowed_hosts = os.getenv('ALLOWED_HOSTS')
allowed_hosts = [h.strip() for h in allowed_hosts.split(',') if h.strip()] if allowed_hosts else ['*']
allowed_hosts = allowed_hosts if allowed_hosts else ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_hosts,        # List of allowed origins
    allow_credentials=True,             # Allow cookies, authorization headers, etc.
    allow_methods=['GET', 'POST'],      # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],                # Allow all headers
)



async def get_orderbooks(w: Worker, db_w: DBWorker):
    """
        Получение всех стаканов (фоновая задача)
    """
    while True:
        try:
            # data = await fetch_external_api(worker)
            # await db_worker.save_data(data)
            
            tracked_shares = await db_w._get(model=TrackedShare)
            
            
        except asyncio.CancelledError:
            
            break
        except Exception as e:
            print(f"Background task error: {e}")
        
        await asyncio.sleep(3)





# -------------------------- Методы настройки приложения ------------------------------
# 1)
@app.post('/get_formal_shares')
async def get_formal_shares(data: dict = Body(...),
                    w: Worker = Depends(get_worker),
                    db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод получение списка акций от API и занесение в БД.
        данные (фильтр) в body:
        {
            "classCode": "TQBR"
        }
    '''
    # фильтр, проверка вхождения элементов
    def check_nested_elem(d1, d2):
        for k in d2:
            if k in d1:
                if isinstance(d2[k], (list, tuple)):
                    if d1[k] not in d2[k]:
                        return False
                elif d1[k] != d2[k]:
                    return False
        return True

    service='InstrumentsService'
    method='Shares'
    result = await send_request(w, Task(service=service, method=method))
    
    if result:
        shares = result.get('instruments', None)

        shares_list = []
        for share in shares:
            if check_nested_elem(share, data):
                new_share = Share(
                        figi = share.get('figi', None),
                        ticker = share.get('ticker', None),
                        class_code = share.get('classCode', None),
                        lot = share.get('lot', None),
                        currency = share.get('currency', None),
                        name = share.get('name', None),
                        cor = share.get('countryOfRisk', None),
                        cor_name = share.get('countryOfRiskName', None),
                        sector = share.get('sector', None)
                    )
                shares_list.append(new_share)
        return await db_w._add(items=shares_list)

    return result



# 2)
@app.post('/set_tracked_shares')
async def set_tracked_shares(db_w: DBWorker = Depends(get_db_worker)):
    '''
        Перенос инструментов в отслеживаемые
    '''
    shares = await db_w._get(model=Share)

    tracked_shares_list = []
    
    if shares:
        for share in shares:
            new_tracked_share = TrackedShare(
                share_id = share.id,
                share=share
            )
            tracked_shares_list.append(new_tracked_share)
        
        return await db_w._add(items=tracked_shares_list)
    
    return None

# -------------------------------------------------------------------------------------




# ------------- Tests -----------------------------------------------------------------
@app.get('/test_concurrency')
async def test_concurrency(w: Worker = Depends(get_worker)):
    '''
        Тестовый эндпоинт для проверки конкурентности
    '''
    figis = ['BBG004731489'] * 100
    filters = {'depth': 10}
    
    tasks = [
        send_request(w, Task(
            service='MarketDataService',
            method='GetOrderBook',
            params={'instrumentId': figi, 'depth': filters['depth']}
        ))
        for figi in figis
    ]
    
    start = time.time()
    results = await asyncio.gather(*tasks)
    total_time = time.time() - start
    
    return {
        "total_time": total_time,
        "count": len(results),
        "results": results[:1]
    }


@app.get('/test_get_one')
async def test_get_one(db_w: DBWorker = Depends(get_db_worker)):
    '''
        Тест получения одной записи по фильтру
    '''
    result = await db_w._get_one(model=Tile, filters={'id': 1})
    return result


@app.get('/test_get')
async def test_get(db_w: DBWorker = Depends(get_db_worker)):
    '''
        Тест получения списка записей по фильтру
    '''
    result = await db_w._get(model=Share, filters={'id': 552})
    return result


@app.get('/test_delete')
async def test_delete(db_w: DBWorker = Depends(get_db_worker)):
    '''
        Тест удаления списка записей по фильтру
    '''
    result = await db_w._delete(model=Share, filters={'id__gte': 1})
    return result

# -----------------------------------------------------------------------------------


## методы для React
## данные для запросов от React передаются в теле запроса body
async def send_request(w: Worker, task: Task | None = None):
    response = None
    try:
        r, extras = await w.getResponse(task)
        response = json.loads(r.content.decode())
    except Exception as e:
        print(f"Error in send_request method: {e}")
    return response



async def send_requests(w: Worker, 
                        tasks: list[Task] | None = None,
                        max_active_tasks: int = 5):
    # semaphore = asyncio.Semaphore(max_active_tasks)
    
    response = None
    try:
        worker_tasks = [w.getResponse(task) for task in tasks]
        worker_response = await asyncio.gather(*worker_tasks)

        response = [(json.loads(resp.content.decode()), extras)
                    for resp, extras in worker_response if resp is not None]

    except Exception as e:
        print(f"Error in send_requests method: {e}")
    return response





@app.post('/get_shares')
async def get_shares(db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод получения списка акций из БД.
    '''
    result = await db_w._get(model=Share, order_fields=['ticker'])
    return result



@app.post('/get_tiles')
async def get_tiles(db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод получение списка плиток из БД. 
    '''
    result = await db_w._get(model=Tile)
    return result



@app.post('/add_tile')
async def add_tile(data: dict = Body(...),
                    db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод добавления плитки в БД.
    '''
    id_share = data.get('id_share', None)
    num_cell = data.get('num_cell', None)
    period_upd = data.get('period_upd', None)
    limit = data.get('limit', None)
    depth = data.get('depth', None)

    share = await db_w._get_one(model=Share, filters={'id': id_share})
    
    new_tile = Tile(
        share_id=id_share,
        share=share,
        period_upd=period_upd,
        limit=limit,
        depth=depth,
        num_cell=num_cell

    )

    await db_w._add(items=[new_tile])
    return True



@app.post('/remove_tile')
async def remove_tile(data: dict = Body(...), 
                    db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод удаления плитки из БД.
    '''
    num_cell = data.get('num_cell', None)
    res = await db_w._delete(model=Tile, filters={'num_cell': num_cell})
    return res



@app.post('/get_orderbook_tile')
async def get_orderbook_tile(data: dict = Body(...), 
                        w: Worker = Depends(get_worker),
                        db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод получение информации по стакану. 
    '''
    num_cell = data.get('num_cell', None)
    tile = await db_w._get_one(model=Tile, filters={'num_cell': num_cell})

    service = 'MarketDataService'
    method='GetOrderBook'
    instrumentId = tile.share.figi  # figi, ticker_classCode
    depth = tile.depth

    task = send_request(w, Task(service=service, method=method,
                params={'instrumentId': instrumentId, 'depth': depth}))

    result = await task

    mx_volume = 0
    price = 0
    state = ''

    for side in ['bids', 'asks']:
        items = result.get(side, None)
        for item in items:
            volume = int(item['quantity'])
            if volume >= mx_volume:
                mx_volume = volume
                price = float(item['price']['units']) + (int(item['price']['nano']) / 1000000000)
                state = side[:-1]

    return {'vol': mx_volume, 'price': f'{price:.2f}', 'state': state}



@app.post('/get_orderbook_tiles')
async def get_orderbook_tiles(data: dict = Body(...),
                        w: Worker = Depends(get_worker),
                        db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод получение информации по стаканам.
    '''

    nums_cells = data.get('nums_cells', None)

    tiles = await db_w._get(model=Tile, filters={'num_cell__in': nums_cells})

    service = 'MarketDataService'
    method='GetOrderBook'

    back_tasks = [Task(service=service, method=method,
                params={'instrumentId': tile.share.figi, 'depth': tile.depth},
                extras={'num_cell': tile.num_cell}) 
                for tile in tiles]

    back_results = await send_requests(w, back_tasks)

    #
    results = {}
    for back_result in back_results:
        mx_volume = 0
        price = 0
        state = ''

        for side in ['bids', 'asks']:
            items = back_result[0].get(side, None)
            for item in items:
                volume = int(item['quantity'])
                if volume >= mx_volume:
                    mx_volume = volume
                    price = float(item['price']['units']) + (int(item['price']['nano']) / 1000000000)
                    state = side[:-1]

        results.update({back_result[1].get('num_cell'): 
                        {'vol': mx_volume, 'price': f'{price:.2f}', 'state': state}})
    
    return results