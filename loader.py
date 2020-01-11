import os


class Loader(object):
    def __init__(self, config):
        self.config = config

    def get_file(self, path, symbol):
        f = os.path.join(os.path.split(__file__)[0], os.path.join(path, symbol))
        return f

    def get_symbols(self):
        f = open(self.config.tickerSymbols, encoding='utf-8')
        symbols = f.read().splitlines()
        return symbols
