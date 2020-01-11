from abc import ABC, abstractmethod


class AbstractScraper(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def scrape(self, ticker):
        pass

