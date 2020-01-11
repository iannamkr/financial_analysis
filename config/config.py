import confuse


class Config(object):
    def __init__(self):
        config = confuse.Configuration('FinancialAnalysis', __name__)
        self.start = config['stock']['period']['start'].get()
        self.end = config['stock']['period']['end'].get()
        self.tickerSymbols = config['file']['tickerSymbols'].get()
        self.fetchedTicker = config['file']['fetchedTicker'].get()
        self.processedTicker = config['file']['processedTicker'].get()

        # self.financials = config['file']['financials'].get()
        # self.balance = config['file']['balance'].get()
        # self.cashflow = config['file']['cashflow'].get()
        # self.fetchedFianance = config['file']['fetchedFianance'].get()
        # self.processedFianance = config['file']['processedFianance'].get()

    def get_tickers(self):
        pass

    def get_urls(self):
        pass
