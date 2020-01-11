from fetcher.abstract.fetcher import AbstractFetcher
from pandas_datareader import data


class YahooFinanceFetcher(AbstractFetcher):
    def __init__(self, config):
        self.config = config

    def fetch_all(self, symbols):
        stocks = []
        [stocks.append(self.fetch(symbol)) for symbol in symbols]
        return stocks

    def fetch(self, symbol, save=True):
        stock = data.get_data_yahoo(symbol, self.config.start, self.config.end)
        stock.to_csv(self.config.fetchedTicker + '/' + symbol)
        return stock
