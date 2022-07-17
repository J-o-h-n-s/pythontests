#from importlib.metadata import SelectableGroups
#from tkinter import SEL_LAST
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine('sqlite:///Liveprice.db')

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

in_position = False
trades = "0"
cum_profit = "0"

while True:
    df = pd.read_sql('ETHUSDT', engine)
    last_price = df.price.iloc[-1]
    cum_profit = float(cum_profit)
    trades = int(trades)
    if not in_position:
        #if last_price > df.price.mean():
        buyprice = last_price
        in_position = True
        print('Bought ETH @ ' +str(buyprice) + 'USDT at ' + current_time)
    if in_position:
        if last_price > 1.003 * buyprice or last_price < 0.997 * buyprice:
            sellprice = last_price
            profit = sellprice - buyprice
            in_position = False
            print('Sold ETH @ '+str(sellprice) + 'USDT at ' + current_time)
            trades = trades + (1)
            print('Trades completed: ' + str(trades))
            if profit > 0.00000000000000000000000000000000000000001:
                print('Profit is: ' + str(profit) + 'USDT')
                cum_profit = cum_profit + float(profit)
                print('Cumulative profit:' + str(cum_profit) + 'USDT')

            else:
                print('Loss is: ' + str(profit) + 'USDT')
                cum_profit = cum_profit + float(profit)
                print('Cumulatice profit:' + str(cum_profit) + 'USDT')
