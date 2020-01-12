from abc import ABC, abstractmethod


class AbstractPortfolio(ABC):
    @abstractmethod
    def preprocess(self):
        raise NotImplementedError

    @abstractmethod
    def get_portfolio(self, symbol):
        raise NotImplementedError

