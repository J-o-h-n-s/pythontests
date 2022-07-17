#%run keys.ipynb



from binance import Client
import pandas as pd

Client = Client(API_KEY, API_SECRET)

posframe = pd.read_csv('positions.csv')

posframe

def changepos(curr, buy=True):
    if buy:
        posframe.loc[posframe.Currency == curr, 'position'] = 1
    else:
        posframe.loc[posframe.Currency == curr, 'position'] = 0

    posframe.to_csv('position', index=False)

def gethourlydata(symbol):
    frame = pd.DataFrame(Client.get_historical_klines(symbol,
                                                        '1h'
                                                        '25 hours ago UTC'))
    frame = frame.iloc[:,:5]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close']
    frame[['Open', 'High', 'Low', 'Close']] = frame[['Open', 'High', 'Low', 'Close']].astype(float)
    frame.Time = pd.pd.to_datetime(frame.Time, unti='ms')
    return frame

gethourlydata('BTCUSDT')

df = gethourlydata('BTCUSDT')

def applytechnicals(df):
    df['FasSMA']

