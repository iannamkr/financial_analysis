from abstract.fetcher import AbstractFetcher
from pandas_datareader import data


class YahooFinanceFetcher(AbstractFetcher):
    def __init__(self, config):
        self.config = config

    def fetch_all(self, symbols):
        stocks = {}
        for symbol in symbols:
            stocks[symbol] = self.fetch(symbol)
        return stocks

    def fetch(self, symbol):
        stock = data.get_data_yahoo(symbol, self.config.start, self.config.end)
        return stock
