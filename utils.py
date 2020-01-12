import os


class FileUtils(object):
    def __init__(self, config):
        self.config = config

    def get_file(self, path, symbol):
        f = os.path.join(os.path.split(__file__)[0], os.path.join(path, symbol))
        return f

    def get_symbols(self):
        f = open(self.config.tickerSymbols, encoding='utf-8')
        symbols = f.read().splitlines()
        return symbols

    @staticmethod
    def save_file(df, dir, symbol):
        os.makedirs(dir,  exist_ok=True)
        path = os.path.join(dir, symbol)
        df.to_csv(path, mode='w')

