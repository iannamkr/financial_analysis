from abstract.portfolio import AbstractPortfolio

import pandas as pd

from utils import FileUtils
from stockstats import StockDataFrame as Sdf


class TechnicalAnalysisPortfolio(AbstractPortfolio):
    def __init__(self, config, symbols):
        self.config = config
        self.symbols = symbols
        self.stocks = {}

        loader = FileUtils(config)
        for symbol in symbols:
            f = loader.get_file(config.fetchedTicker, symbol)
            self.stocks[symbol] = (Sdf.retype(pd.read_csv(f)))

        self.preprocess()

    def preprocess(self):
        features = list(self.config.stock['features'].values())

        for feature in features:
            for symbol, stock in self.stocks.items():
                stock[str(feature)]

    def get_portfolio(self, symbol):
        return self.stocks[symbol]


