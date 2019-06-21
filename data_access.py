
import pandas_datareader.data as web
import datetime

def read_yahooData(etf):
    start = datetime.datetime.today() - datetime.timedelta(days=120)
    # end = datetime.datetime.today()
    price = web.DataReader(etf, 'yahoo', start)
    # print(price['Adj Close'])
    return price['Adj Close']
