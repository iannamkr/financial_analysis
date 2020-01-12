import confuse


class Config(object):
    def __init__(self):
        config = confuse.Configuration('FinancialAnalysis', __name__)
        self.pool_size = config['system']['poolSize']

        self.stock = config['stock']
        self.start = config['stock']['period']['start'].get()
        self.end = config['stock']['period']['end'].get()

        self.tickerSymbols = config['file']['tickerSymbols'].get()

        self.fetchedTicker = config['file']['fetchedTicker'].get()
        self.crawledFinancials = config['file']['crawledFinancials'].get()

        self.processedTicker = config['file']['processedTicker'].get()
        self.processedFinancials = config['file']['processedFinancials'].get()

        self.financials = config['url']['financials'].get()

    def get_tickers(self):
        pass

    def get_urls(self):
        pass
