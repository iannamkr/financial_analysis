from abstract.frontier import AbstractFrontier


class YahooFinanceFrontier(AbstractFrontier):
    def __init__(self, config, symbols):
        self.config = config
        self.symbols = symbols
        self.urls = self.init_urls(symbols)
        self.robots = self.init_robots(symbols)
        self.pool_size = config.pool_size if len(symbols) > config.pool_size else len(symbols)

    def init_urls(self, symbols):
        urls = {}
        for symbol in symbols:
            urls[symbol] = self.config.financials.format(symbol)
        return urls

    def init_robots(self, symbols):
        import urllib.robotparser
        rp = urllib.robotparser.RobotFileParser()

        robots = {}
        for symbol in symbols:
            rp.set_url(self.urls[symbol])
            rp.read()
            robots[symbol] = rp
        return robots

    def get_robots(self):
        return self.robots

    def get_seed(self, symbol):
        return self.urls.pop(symbol)

    def get_robots(self):
        return self.robots
