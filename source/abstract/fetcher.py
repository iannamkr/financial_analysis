from abc import ABC, abstractmethod


class AbstractFetcher(ABC):
    @abstractmethod
    def fetch_all(self, symbols):
        raise NotImplementedError

    @abstractmethod
    def fetch(self, symbol):
        raise NotImplementedError

