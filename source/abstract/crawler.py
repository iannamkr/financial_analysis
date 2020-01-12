from abc import ABC, abstractmethod


class AbstractCrawler(ABC):
    @abstractmethod
    def crawl(self, symbol, url, path):
        raise NotImplementedError
