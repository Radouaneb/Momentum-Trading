import urllib3
import pandas

def get_ETFSymbols(source):
    if source.lower() == 'nasdaq':
        etf = pandas.read_csv('https://www.nasdaq.com/investing/etfs/etf-finder-results.aspx?download=Yes')['Symbol'].values
        return etf[0:]
