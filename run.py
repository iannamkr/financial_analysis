import os
from config.config import Config
from fetcher.YahooFinanceFetcher import YahooFinanceFetcher


def save_file(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, mode='w')


if __name__ == '__main__':
    config = Config()

    f = open(config.tickerSymbols, encoding='utf-8')
    symbols = f.read().splitlines()

    yahooFinanceFetcher = YahooFinanceFetcher(config)

    fetched_tickers = yahooFinanceFetcher.fetch(symbols[0])
    fetched_tickers.to_csv(config.fetchedTicker + '/' + symbols[0] + ".csv")



