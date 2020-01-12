from abc import ABC, abstractmethod


class AbstractFrontier(ABC):
    @abstractmethod
    def get_seed(self, symbol):
        raise NotImplementedError

    @abstractmethod
    def init_urls(self, symbols):
        raise NotImplementedError

    @abstractmethod
    def init_robots(self, symbols):
        raise NotImplementedError

