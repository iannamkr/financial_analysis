import os
import logging
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from pandas_datareader import data
from stockstats import StockDataFrame as Sdf


yf.pdr_override()
log = logging.getLogger(__name__)

START = '2010-01-01'
END = '2019-12-30'
FEATURES = ['open', 'close', 'high', 'low', 'volumn', 'amount']
PATH = "../resources/download/{}_{}".format(START, END)


def get_filename(ticker, tp='raw'):
    return "{}/{}_{}.csv".format(PATH, ticker, tp)


def get_file(filename):
    return os.path.join(os.path.split(__file__)[0], os.path.join(PATH, filename))


def save_file(df, filename):
    df.to_csv(filename, mode='w')


def fetch(ticker):
    return data.get_data_yahoo(ticker, START, END)


def load_stock_stat(ticker):
    return Sdf.retype(pd.read_csv(get_file('{}_raw.csv'.format(ticker))))


def analze(stock):
    import numpy as np
    from scipy.stats import norm

    stock['LogReturn'] = np.log(stock['close']).shift(-1) - np.log(stock['close'])
    mean = stock['LogReturn'].mean()
    sigma = stock['LogReturn'].std(ddof=1)

    def show_MA50():
        stock['ma50'] = stock['close'].rolling(50).mean()
        # plot the moving average
        plt.figure(figsize=(10, 8))
        stock['ma50'].loc[START:END].plot(label='MA50')
        stock['close'].loc[START:END].plot(label='Close')
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


def download(ticker):
    filename = get_filename(ticker, 'raw')
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    df = fetch(ticker)
    save_file(df, filename)


if __name__ == '__main__':
    f = open('../resources/stock_list.txt', encoding='utf-8')

    # download raw
    # [download(ticker) for ticker in f.read().splitlines()]

    # analyze
    ticker = 'AMZN'
    stock = load_stock_stat(ticker)
    analze(stock)

