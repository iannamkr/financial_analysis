from fetcher.abstract.fetcher import AbstractFetcher
from pandas_datareader import data


class YahooFinanceFetcher(AbstractFetcher):
    def __init__(self, config):
        self.start = config.start
        self.end = config.end

    def fetch_all(self, tickers):
        fetch = []
        [fetch.append(self.fetch(ticker)) for ticker in tickers]
        return fetch

    def fetch(self, ticker):
        return data.get_data_yahoo(ticker, self.start, self.end)
