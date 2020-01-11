import os
import logging
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from config.config import Config
from stockstats import StockDataFrame as Sdf


yf.pdr_override()
log = logging.getLogger(__name__)


def get_file(path, symbol, fmt='csv'):
    return os.path.join(os.path.split(__file__)[0], os.path.join(path, symbol + '.' + fmt))


def load_stock_stat(symbol):
    return Sdf.retype(pd.read_csv(get_file(fetchedTicker, symbol)))


def analze(stock):
    stock['LogReturn'] = np.log(stock['close']).shift(-1) - np.log(stock['close'])
    mean = stock['LogReturn'].mean()
    sigma = stock['LogReturn'].std(ddof=1)
    start = config.start
    end = config.end

    def show_MA50():
        stock['ma50'] = stock['close'].rolling(50).mean()

        # plot the moving average
        plt.figure(figsize=(10, 8))
        stock['ma50'].loc[start:end].plot(label='MA50')
        stock['close'].loc[start:end].plot(label='Close')
        plt.legend()
        plt.show()

    def show_distribution_log_returns():
        stock['LogReturn'] = np.log(stock['close']).shift(-1) - np.log(stock['close'])

        density = pd.DataFrame()
        density['x'] = np.arange(stock['LogReturn'].min() - 0.01, stock['LogReturn'].max() + 0.01, 0.001)
        density['pdf'] = norm.pdf(density['x'], mean, sigma)

        stock['LogReturn'].hist(bins=50, figsize=(15, 8))
        plt.plot(density['x'], density['pdf'], color='red')
        plt.show()

    def show_up_down_log_returns():
        stock['LogReturn'].plot(figsize=(20, 8))
        plt.axhline(0, color='red')
        plt.show()

    def print_prob_stock_price_drops_in(x):
        return norm.cdf(-x, mean, sigma)

    show_MA50()
    show_distribution_log_returns()
    show_up_down_log_returns()
    print_prob_stock_price_drops_in(0.035)


if __name__ == '__main__':
    config = Config()

    f = open(config.tickerSymbols, encoding='utf-8')
    symbols = f.read().splitlines()

    fetchedTicker = config.fetchedTicker
    processedTicker = config.processedTicker

    stock = load_stock_stat(symbols[0])

    analze(stock)

