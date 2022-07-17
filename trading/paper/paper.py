import pandas as pd
from sqlalchemy import create_engine
import unicorn_binance_websocket_api as unicorn

engine = create_engine('sqlite:///Liveprice.db')
ubwa = unicorn.BinanceWebSocketApiManager(exchange = 'binance.com')
ubwa.create_stream('kline_1m', 'ETHUSDT', output='UnicornFy')

data = ubwa.pop_stream_data_from_stream_buffer()

def SQLimport(data):
    time = pd.to_datetime(data['event_time'], unit='ms')
    close = float(data['kline']['close_price'])
    frame = pd.DataFrame({'timestamp':time, 'price':close}, index=[0])
    frame.to_sql(data['symbol'], engine, index=False, if_exists='append')

    


while True:
    data = ubwa.pop_stream_data_from_stream_buffer()
    if data and len(data) > 3:
        SQLimport(data)