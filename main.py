from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from tinvst import Task, Worker
import uvicorn
from dotenv import load_dotenv
import os


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

load_dotenv()
worker = Worker(token=os.getenv('TOKEN'), url=os.getenv('SANDBOX_URL'))


def get_worker():
    if worker is None:
        raise Exception("Worker not initialized")
    return worker



@app.get('/')
async def lead(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("base.html", context=context)



@app.get('/get_shares')
async def getshares(w: Worker = Depends(get_worker)):
    t = Task(service='InstrumentsService', method='Shares')
    return await w.getResponse(t)



@app.get('/show_shades')
def showshades():
    ...


@app.get('/show_tiles')
async def showtiles(request: Request, w: Worker = Depends(get_worker)):
    
    #TODO Real data (NOW are fictive params and filters)
    figis = ['BBG004731489', 'BBG004RVFCY3', 'TCS90A0JQUZ6']
    filters = {'depth': 20, 'level_vol_bids': 1000, 'level_vol_asks': 1000}
    
    ts = [Task(service='MarketDataService', method='GetOrderBook', 
                params={'instrumentId': figi, 'depth': filters['depth']}) for figi in figis]    
    
    response: list = await w.getResponse(*ts)
    
    # parsing response
    instruments = []
    for share in response:
        instrument = {}
        prices = {}
        asks = share['asks']
        bids = share['bids']

        if len(bids) == len(asks):
            for i in range(len(bids)):
                
                #
                bid_price = float(bids[i]['price']['units']) + (bids[i]['price']['nano'] / 1000000000)
                bid_quantity = int(bids[i]['quantity'])
                if bid_quantity >= filters.get('level_vol_bids', 0):
                    if bid_price not in prices:
                        prices[bid_price] = {'ask': '-'}
                if bid_price in prices:
                    prices[bid_price].update({'bid': bid_quantity})
                
                #
                ask_price = float(asks[i]['price']['units']) + (asks[i]['price']['nano'] / 1000000000)
                ask_quantity = int(asks[i]['quantity'])
                if ask_quantity >= filters.get('level_vol_asks', 0):
                    if ask_price not in prices:
                        prices[ask_price] = {'bid': '-'}
                if ask_price in prices:
                    prices[ask_price].update({'ask': ask_quantity})


        prices = dict(sorted(prices.items(), reverse=True))
        
        for k in list(prices.keys()):
            prices[f'{k:.2f}'] = prices.pop(k)
        
        if prices:
            instrument = {'figi': share['figi'],
                            'last_price': float(share['lastPrice']['units']) + (share['lastPrice']['nano'] / 1000000000),
                            'ticker': share['ticker'],
                            'class_code': share['classCode'],
                            'last_price_time': share['lastPriceTs'],
                            'order_book_upd_time': share.get('orderbookTs', '-'),
                            'prices': prices,
                            'depth': filters.get('depth', '-'),
                            'level_vol_bids': filters.get('level_vol_bids', 0), 
                            'level_vol_asks': filters.get('level_vol_asks', 0)
                        }
            instruments.append(instrument)

    context = {"request": request, 'instruments': instruments}
    return templates.TemplateResponse("show_tiles.html", context=context)



if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)