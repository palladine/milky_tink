from fastapi import FastAPI, Depends
from dotenv import load_dotenv
import os
import json
import asyncio
import time
from tinvest import Task, Worker
from .models import Tile
from .db_models import Share
from .db_worker import DBWorker


app = FastAPI()

load_dotenv()

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


# @app.get('/show_tiles')
# async def showtiles(request: Request, w: Worker = Depends(get_worker)):
    
#     #TODO Real data (NOW are fictive params and filters)
#     figis = ['BBG004731489', 'BBG004RVFCY3', 'TCS90A0JQUZ6']*3
#     filters = {'depth': 20, 'level_vol_bids': 3000, 'level_vol_asks': 3000}
    
#     tasks = [
#             send_request(w, Task(service='MarketDataService', 
#                 method='GetOrderBook', 
#                 params={'instrumentId': figi, 'depth': filters['depth']}
#                 ))
#                 for figi in figis]
    
#     response = await asyncio.gather(*tasks)
    
#     # parsing response
#     instruments = []
#     for share in response:
#         instrument = {}
#         prices = {}
#         asks = share['asks']
#         bids = share['bids']

#         if len(bids) == len(asks):
#             for i in range(len(bids)):
                
#                 #
#                 bid_price = float(bids[i]['price']['units']) + (bids[i]['price']['nano'] / 1000000000)
#                 bid_quantity = int(bids[i]['quantity'])
#                 if bid_quantity >= filters.get('level_vol_bids', 0):
#                     if bid_price not in prices:
#                         prices[bid_price] = {'ask': ''}
#                 if bid_price in prices:
#                     prices[bid_price].update({'bid': bid_quantity})
                
#                 #
#                 ask_price = float(asks[i]['price']['units']) + (asks[i]['price']['nano'] / 1000000000)
#                 ask_quantity = int(asks[i]['quantity'])
#                 if ask_quantity >= filters.get('level_vol_asks', 0):
#                     if ask_price not in prices:
#                         prices[ask_price] = {'bid': ''}
#                 if ask_price in prices:
#                     prices[ask_price].update({'ask': ask_quantity})


#         prices = dict(sorted(prices.items(), reverse=True))
        
#         if prices:
#             for k in list(prices.keys()):
#                 prices[f'{k:.2f}'] = prices.pop(k)

#             instrument = {'figi': share['figi'],
#                             'last_price': float(share['lastPrice']['units']) + (share['lastPrice']['nano'] / 1000000000),
#                             'ticker': share['ticker'],
#                             'class_code': share['classCode'],
#                             'last_price_time': share['lastPriceTs'],
#                             'order_book_upd_time': share.get('orderbookTs', '-'),
#                             'prices': prices,
#                             'depth': filters.get('depth', '-'),
#                             'level_vol_bids': filters.get('level_vol_bids', 0), 
#                             'level_vol_asks': filters.get('level_vol_asks', 0)
#                         }
#             instruments.append(instrument)

#     context = {"request": request, 'instruments': instruments}
#     return templates.TemplateResponse("show_tiles.html", context=context)




@app.get('/test_concurrency')
async def test_concurrency():
    '''
        Тестовый эндпоинт для проверки конкурентности
    '''
    figis = ['BBG004731489', 'BBG004RVFCY3', 'TCS90A0JQUZ6'] * 33
    filters = {'depth': 20}
    
    tasks = [
        send_request(worker, Task(
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


@app.get('/test_get')
async def test_get(db_w: DBWorker = Depends(get_db_worker)):
    result = await db_w._get_one(model='Share', filters={'id': 1})
    return result




## методы для React
## данные для запросов от React в теле запроса

async def send_request(w: Worker, task: None | Task = None):
    try:
        response = await w.getResponse(task)
        return json.loads(response.content.decode())
    except Exception as e:
        print(f"Error in send_request method: {e}")



@app.post('/get_shares')
async def get_shares(w: Worker = Depends(get_worker),
                    db_w: DBWorker = Depends(get_db_worker)):
    '''
        Метод получение списка акций. 
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
        return await db_w._add(model='Share', items=shares_list)

    return result



@app.post('/get_info_tile')
async def get_info_tile(tile: Tile, w: Worker = Depends(get_worker)):
    '''
        Метод получение информации по стакану. 
        Формирование плитки.
    '''
    # tile.id_tile - id плитки
    
    # Данные фиктивные
    # TODO Получение реальных данных из БД
    service = 'MarketDataService'
    method='GetOrderBook'
    instrumentId = 'TCS90A0JQUZ6' # figi, ticker_classCode
    depth = 20

    task = send_request(w, Task(service=service, method=method,
                params={'instrumentId': instrumentId, 'depth': depth}))

    result = await task
    return result

