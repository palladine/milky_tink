from fastapi import FastAPI, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import json
import asyncio
import time
from tinvest import Task, Worker
from .db_models import Share, Tile
from .db_worker import DBWorker


app = FastAPI()

load_dotenv()


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



worker = Worker(token=os.getenv('TOKEN'), url=os.getenv('SANDBOX_URL'))
db_worker = DBWorker(
    db_user = os.getenv('DB_USER'),
    db_pass = os.getenv('DB_PASSWORD'),
    db_host = os.getenv('DB_HOST'),
    db_port = os.getenv('DB_PORT'),
    db_name = os.getenv('DB_NAME')
)


def get_worker():
    if worker is None:
        raise Exception("Worker not initialized")
    return worker


def get_db_worker():
    if db_worker is None:
        raise Exception("Worker not initialized")
    return db_worker


# ------------- Tests -----------------------------------------------------------------
@app.get('/test_concurrency')
async def test_concurrency(w: Worker = Depends(get_worker)):
    '''
        Тестовый эндпоинт для проверки конкурентности
    '''
    figis = ['BBG004731489', 'BBG004RVFCY3', 'TCS90A0JQUZ6'] * 33
    filters = {'depth': 20}
    
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
    result = await db_w._delete(model=Share, filters={'id__gte': 1911})
    return result

# -----------------------------------------------------------------------------------


## методы для React
## данные для запросов от React в теле запроса

async def send_request(w: Worker, task: None | Task = None):
    response = None
    try:
        response = await w.getResponse(task)
        return json.loads(response.content.decode())
    except Exception as e:
        print(f"Error in send_request method: {e}")



@app.post('/get_api_shares')
async def get_api_shares(w: Worker = Depends(get_worker),
                    db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод получение списка акций от API и занесение в БД. 
    '''
    service='InstrumentsService'
    method='Shares'
    task = send_request(w, Task(service=service, method=method))
    result = await task
    
    if result:
        shares = result.get('instruments', None)

        shares_list = []
        for _share in shares:
            new_share = Share(
                    figi = _share.get('figi', None),
                    ticker = _share.get('ticker', None),
                    class_code = _share.get('classCode', None),
                    lot = _share.get('lot', None),
                    currency = _share.get('currency', None),
                    name = _share.get('name', None),
                    cor = _share.get('countryOfRisk', None),
                    cor_name = _share.get('countryOfRiskName', None),
                    sector = _share.get('sector', None)
                )
            shares_list.append(new_share)
        return await db_w._add(items=shares_list)

    return result



@app.post('/get_shares')
async def get_shares(db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод получения списка акций.
    '''
    result = await db_w._get(model=Share, order_fields=['ticker'])
    return result



@app.post('/get_tiles')
async def get_tiles(db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод получение списка плиток. 
    '''
    result = await db_w._get(model=Tile)
    return result



@app.post('/add_tile')
async def add_tile(datas: dict = Body(...),
                    db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод добавления плитки в БД.
    '''
    id_share = datas.get('id_share', None)
    num_cell = datas.get('num_cell', None)
    period_upd = datas.get('period_upd', None)
    limit = datas.get('limit', None)

    share = await db_w._get_one(model=Share, filters={'id': id_share})
    
    new_tile = Tile(
        share_id=id_share,
        share=share,
        period_upd=period_upd,
        limit=limit,
        num_cell=num_cell
    )

    await db_w._add(items=[new_tile])
    return True



@app.post('/remove_tile')
async def remove_tile(datas: dict = Body(...), 
                    db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод удаления плитки из БД.
    '''
    num_cell = datas.get('num_cell', None)
    res = await db_w._delete(model=Tile, filters={'num_cell': num_cell})
    return res



@app.post('/get_info_tile')
async def get_info_tile(datas: dict = Body(...), 
                        w: Worker = Depends(get_worker),
                        db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод получение информации по стакану. 
        Формирование плитки.
    '''
    num_cell = datas.get('num_cell', None)
    tile = await db_w._get_one(model=Tile, filters={'num_cell': num_cell})

    service = 'MarketDataService'
    method='GetOrderBook'
    instrumentId = tile.share.figi  # figi, ticker_classCode
    depth = 20

    task = send_request(w, Task(service=service, method=method,
                params={'instrumentId': instrumentId, 'depth': depth}))

    result = await task
    
    # filters
    mx_volume = 0
    price = 0
    state = ''

    bids = result.get('bids', None)
    asks = result.get('asks', None)

    if bids and asks:
        for bid in bids:
            volume = int(bid['quantity'])
            if volume >= mx_volume:
                mx_volume = volume
                price = float(bid['price']['units']) + (int(bid['price']['nano']) / 1000000000)
                state = 'bid'
        for ask in asks:
            volume = int(ask['quantity'])
            if volume >= mx_volume:
                mx_volume = volume
                price = float(ask['price']['units']) + (int(ask['price']['nano']) / 1000000000)
                state = 'ask'

    return {'vol': mx_volume, 'price': f'{price:.2f}', 'state': state}


