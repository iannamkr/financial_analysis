import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


class Visualizer(object):
    @staticmethod
    def show_moving_average(stock, start, end, days=[3, 10, 30, 120]):
        plt.figure(figsize=(10, 8))

        for rolling in days:
            ma = 'ma{}'.format(rolling)
            stock[ma] = stock['close'].rolling(rolling).mean()
            stock[ma].loc[start:end].plot(label=ma)

        stock['close'].loc[start:end].plot(label='Close')
        plt.legend()
        plt.show()

    @staticmethod
    def show_distribution_log_returns(stock):
        stock['LogReturn'] = np.log(stock['close']).shift(-1) - np.log(stock['close'])
        mean = stock['LogReturn'].mean()
        sigma = stock['LogReturn'].std(ddof=1)

        density = pd.DataFrame()
        density['x'] = np.arange(stock['LogReturn'].min() - 0.01, stock['LogReturn'].max() + 0.01, 0.001)
        density['pdf'] = norm.pdf(density['x'], mean, sigma)

        stock['LogReturn'].hist(bins=50, figsize=(15, 8))
        plt.plot(density['x'], density['pdf'], color='red')
        plt.show()

    @staticmethod
    def show_up_down_log_returns(stock):
        stock['LogReturn'] = np.log(stock['close']).shift(-1) - np.log(stock['close'])
        stock['LogReturn'].plot(figsize=(20, 8))
        plt.axhline(0, color='red')
        plt.show()
