from fastapi import FastAPI, Depends, Body, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import json
import asyncio
import time
from tinvest import Task, RESTClient, GRPCClient, GRPCStreamClient, utils, get_error_by_code
from .db_models import Share, TrackedShare, Tile
from .db_client import DBClient
from contextlib import asynccontextmanager
from fastapi.responses import StreamingResponse




load_dotenv()

class AppState:
    def __init__(self):
        self.rest_client: RESTClient | None = None
        self.grpc_client: GRPCClient | None = None
        self.db_client: DBClient | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    state = AppState()

    state.rest_client = RESTClient(
        token=os.getenv('TOKEN'),
        url=os.getenv('SANDBOX_URL')
    )

    state.grpc_client = GRPCClient(
        token=os.getenv('TOKEN'),
        url=os.getenv('GRPC_SANDBOX_URL')
    )
    
    state.db_client = DBClient(
        db_user=os.getenv('DB_USER'),
        db_pass=os.getenv('DB_PASSWORD'),
        db_host=os.getenv('DB_HOST'),
        db_port=os.getenv('DB_PORT'),
        db_name=os.getenv('DB_NAME')
    )


    # секция задач при запуске приложения
    app.state = state
    
    asyncio.create_task(get_orderbooks_stream(state.db_client))
    
    yield

    # секция задач при закрытии приложения




app = FastAPI(lifespan=lifespan)


async def get_client_by_protocol(protocol: str):
    clients = {
        "rest": get_rest_client,
        "grpc": get_grpc_client,
    }

    if protocol not in clients:
        raise HTTPException(status_code=400, 
                            detail=f'{protocol} не поддерживается')
    
    return await clients[protocol.lower()]()


async def get_rest_client() -> RESTClient:
    if not hasattr(app.state, 'rest_client') or app.state.rest_client is None:
        raise RuntimeError(get_error_by_code(700, 'rest_client'))
    return app.state.rest_client

async def get_grpc_client() -> GRPCClient:
    if not hasattr(app.state, 'grpc_client') or app.state.grpc_client is None:
        raise RuntimeError(get_error_by_code(700, 'grpc_client'))
    return app.state.grpc_client

async def get_db_client() -> DBClient:
    if not hasattr(app.state, 'db_client') or app.state.db_client is None:
        raise RuntimeError(get_error_by_code(700, 'db_client'))
    return app.state.db_client




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



# -------------------------- Методы настройки приложения ------------------------------
# 1)
@app.post('/{protocol}/get_formal_shares')
async def get_formal_shares(protocol: str = Path(...),
                            data: dict = Body(...),
                            c: RESTClient | GRPCClient = Depends(get_client_by_protocol),
                            db_c: DBClient = Depends(get_db_client)
                            ):
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

    task_params = {'service': 'InstrumentsService',
                    'method': 'Shares',
                    'params': {}}
    if protocol == 'grpc':
        task_params.update({
            'body_name_request': 'InstrumentsRequest',
            'body_name_response':  'SharesResponse'
        })
    
    result = await send_request(c, Task(**task_params))
    
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
        return await db_c._add(items=shares_list)

    return result


# 2)
@app.post('/set_tracked_shares')
async def set_tracked_shares(db_c: DBClient = Depends(get_db_client)):
    '''
        Перенос инструментов в отслеживаемые
    '''
    shares = await db_c._get(model=Share)

    tracked_shares_list = []
    
    if shares:
        for share in shares:
            new_tracked_share = TrackedShare(
                share_id = share.id,
                share=share
            )
            tracked_shares_list.append(new_tracked_share)
        
        return await db_c._add(items=tracked_shares_list)
    
    return None

# -------------------------------------------------------------------------------------



# --------------------- 
async def get_orderbooks_stream(db_c: DBClient = Depends(get_db_client)):


    instruments = ["SBER_TQBR"]
    params = {
        'instruments': instruments,
        'depth': 50,
        'ping_delay': 20000
    }
    
    task_params = {'service': 'MarketDataStreamService',
                    'method': 'MarketDataServerSideStream',
                    'body_name_request': 'MarketDataServerSideStreamRequest',
                    'body_name_response': 'MarketDataResponse',
                    'params': params,
                }
    stream_client = GRPCStreamClient(token=os.getenv('TOKEN'),
                                    url=os.getenv('GRPC_SANDBOX_URL'))
    

    stream_responses = send_stream_request(stream_client, Task(**task_params))
    
    async for response in stream_responses:
        try:
            data = json.loads(response)

            if 'orderbook' in data:
                # Можно отправить клиентам через WebSocket и т.д.
                # print(data)
                print('+')
        except Exception as e:
            print(response)
# -------------------------







# ------------- Tests -----------------------------------------------------------------
@app.get('/{protocol}/test_concurrency')
async def test_concurrency(protocol: str = Path(...),
                            c: RESTClient | GRPCClient = Depends(get_client_by_protocol)):
    '''
        Тестовый эндпоинт для проверки конкурентности 
        (получение стаканов инструментов)
    '''
    figis = ['BBG004731489'] * 100
    
    tasks = []
    for figi in figis:
        params={'instrumentId': figi, 'depth': 50}
        
        task_params = {
            'service': 'MarketDataService',
            'method': 'GetOrderBook',
            'params': params
        }

        if protocol == 'grpc':
            task_params.update({
                'body_name_request': 'GetOrderBookRequest',
                'body_name_response':  'GetOrderBookResponse'
            })

        tasks.append(
            send_request(c, Task(**task_params))
        )

    start = time.time()
    results = await asyncio.gather(*tasks)
    total_time = time.time() - start
    
    return {
        "total_time": total_time,
        "count": len(results),
        "results": results[:1]
    }


@app.post('/test_get_one')
async def test_get_one(db_c: DBClient = Depends(get_db_client)):
    '''
        Тест получения одной записи по фильтру
    '''
    result = await db_c._get_one(model=Tile, filters={'id': 1})
    return result


@app.post('/test_get')
async def test_get(db_c: DBClient = Depends(get_db_client)):
    '''
        Тест получения списка записей по фильтру
    '''
    result = await db_c._get(model=Share, filters={'id': 552})
    return result


@app.post('/test_delete')
async def test_delete(db_c: DBClient = Depends(get_db_client)):
    '''
        Тест удаления списка записей по фильтру
    '''
    result = await db_c._delete(model=Share, filters={'id__gte': 1})
    return result

# -----------------------------------------------------------------------------------


## методы для React
## данные для запросов от React передаются в теле запроса body
async def send_request(c: RESTClient | GRPCClient, 
                    task: Task | None = None):
    try:
        response = await c.get_response(task)
        return json.loads(response)
    except Exception as e:
        raise TypeError(get_error_by_code(703, e))



async def send_stream_request(c: GRPCStreamClient,
                            task: Task | None = None):
    try:
        async for stream_data in c.get_response(task):
            yield stream_data
    except Exception as e:
        yield get_error_by_code(703, e)



# async def send_requests(w: Worker, 
#                         tasks: list[Task] | None = None,
#                         max_active_tasks: int = 5):
    
#     response = None
    
#     if tasks:
#         # semaphore = asyncio.Semaphore(max_active_tasks)

#         try:
#             worker_tasks = [w.getResponse(task) for task in tasks]
#             worker_response = await asyncio.gather(*worker_tasks, 
#                                                 return_exceptions=True)

#             response = [(json.loads(resp.content.decode()), extras)
#                         for resp, extras in worker_response 
#                         if not isinstance(resp, Exception) 
#                         and resp is not None
#                         and resp.status_code == 200]

#         except Exception as e:
#             print(f"Error in send_requests method: {e}")

#     return response





@app.post('/get_shares')
async def get_shares(db_c: DBClient = Depends(get_db_client)):
    '''
        Метод получения списка акций из БД.
    '''
    result = await db_c._get(model=Share, order_fields=['ticker'])
    return result



@app.post('/get_tiles')
async def get_tiles(db_c: DBClient = Depends(get_db_client)):
    '''
        Метод получение списка плиток из БД. 
    '''
    result = await db_c._get(model=Tile)
    return result



@app.post('/add_tile')
async def add_tile(data: dict = Body(...),
                    db_c: DBClient = Depends(get_db_client)):
    '''
        Метод добавления плитки в БД.
    '''
    id_share = data.get('id_share', None)
    num_cell = data.get('num_cell', None)
    period_upd = data.get('period_upd', None)
    limit = data.get('limit', None)
    depth = data.get('depth', None)

    share = await db_c._get_one(model=Share, filters={'id': id_share})
    
    new_tile = Tile(
        share_id=id_share,
        share=share,
        period_upd=period_upd,
        limit=limit,
        depth=depth,
        num_cell=num_cell

    )

    await db_c._add(items=[new_tile])
    return True



@app.post('/remove_tile')
async def remove_tile(data: dict = Body(...), 
                    db_c: DBClient = Depends(get_db_client)):
    '''
        Метод удаления плитки из БД.
    '''
    num_cell = data.get('num_cell', None)
    res = await db_c._delete(model=Tile, filters={'num_cell': num_cell})
    return res





# @app.post('/get_orderbook_tile')
# async def get_orderbook_tile(data: dict = Body(...), 
#                         w: Worker = Depends(get_worker),
#                         db_w: DBWorker = Depends(get_db_worker)):
#     '''
#         Метод получение информации по стакану. 
#     '''
#     num_cell = data.get('num_cell', None)
#     tile = await db_w._get_one(model=Tile, filters={'num_cell': num_cell})

#     service = 'MarketDataService'
#     method='GetOrderBook'
#     instrumentId = tile.share.figi  # figi, ticker_classCode
#     depth = tile.depth

#     task = send_request(w, Task(service=service, method=method,
#                 params={'instrumentId': instrumentId, 'depth': depth}))

#     result = await task

#     mx_volume = 0
#     price = 0
#     state = ''

#     for side in ['bids', 'asks']:
#         items = result.get(side, None)
#         for item in items:
#             volume = int(item['quantity'])
#             if volume >= mx_volume:
#                 mx_volume = volume
#                 price = float(item['price']['units']) + (int(item['price']['nano']) / 1000000000)
#                 state = side[:-1]

#     return {'vol': mx_volume, 'price': f'{price:.2f}', 'state': state}



# @app.post('/get_orderbook_tiles')
# async def get_orderbook_tiles(data: dict = Body(...),
#                         w: Worker = Depends(get_worker),
#                         db_w: DBWorker = Depends(get_db_worker)):
#     '''
#         Метод получение информации по стаканам.
#     '''

#     nums_cells = data.get('nums_cells', None)

#     tiles = await db_w._get(model=Tile, filters={'num_cell__in': nums_cells})

#     service = 'MarketDataService'
#     method='GetOrderBook'

#     back_tasks = [Task(service=service, method=method,
#                 params={'instrumentId': tile.share.figi, 'depth': tile.depth},
#                 extras={'num_cell': tile.num_cell}) 
#                 for tile in tiles]

#     back_results = await send_requests(w, back_tasks)

#     #
#     results = {}
#     for back_result in back_results:
#         mx_volume = 0
#         price = 0
#         state = ''

#         for side in ['bids', 'asks']:
#             items = back_result[0].get(side, None)
#             for item in items:
#                 volume = int(item['quantity'])
#                 if volume >= mx_volume:
#                     mx_volume = volume
#                     price = float(item['price']['units']) + (int(item['price']['nano']) / 1000000000)
#                     state = side[:-1]

#         results.update({back_result[1].get('num_cell'): 
#                         {'vol': mx_volume, 'price': f'{price:.2f}', 'state': state}})
    
#     return results



# async def get_orderbooks(w: Worker, db_w: DBWorker):
#     """
#         Получение всех стаканов (фоновая задача)
#     """
#     while True:
#         try:
#             tracked_shares = await db_w._get(model=TrackedShare)
#             service = 'MarketDataService'
#             method='GetOrderBook'

#             tasks = [Task(service=service, method=method,
#                 params={'instrumentId': tracked_share.share.figi, 'depth': 50},
#                 extras={'id': tracked_share.id}) 
#                 for tracked_share in tracked_shares]

#             results = await send_requests(w, tasks)

#             for result in results:
#                 filters = result[1]
#                 data = {
#                     'bids': result[0]['bids'],
#                     'asks': result[0]['asks'],
#                 }

#                 # db_w._update()
#                 # print(filters, data)


#         except asyncio.CancelledError:
#             break
#         except Exception as e:
#             print(f"Background task error: {e}")
        
#         await asyncio.sleep(1)