from abc import ABC, abstractmethod


class AbstractFetcher(ABC):
    @abstractmethod
    def fetch_all(self):
        raise NotImplementedError

    @abstractmethod
    def fetch(self, ticker):
        raise NotImplementedError

