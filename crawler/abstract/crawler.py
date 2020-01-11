from abc import ABC, abstractmethod


class AbstractCrawler(ABC):
    @abstractmethod
    def crawl_url(self, url):
        raise NotImplementedError

    @abstractmethod
    def download(self, ticker):
        raise NotImplementedError
