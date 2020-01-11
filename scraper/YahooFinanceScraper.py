from scraper.abstract.scraper import AbstractScraper


class YahooFinanceScraper(AbstractScraper):
    def scrape(self, ticker):
        pass

    def __init__(self, config):
        self.config = config

