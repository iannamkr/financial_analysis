import os
from config.config import Config
from fetcher.YahooFinanceFetcher import YahooFinanceFetcher
from portfolio.portfolio import Portfolio


def save_file(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, mode='w')


if __name__ == '__main__':
    config = Config()

    f = open(config.tickerSymbols, encoding='utf-8')

    symbols = ['IBM', 'GOOG', 'MSFT', 'AAPL', 'INTC']
    fetcher = YahooFinanceFetcher(config)
    fetcher.fetch_all(symbols)

    portfolio = Portfolio(config, symbols)

    from portfolio.visualizer import Visualizer

    apple_portfolio = portfolio.get_portfolio('AAPL')

    Visualizer.show_moving_average(apple_portfolio, '2019-01-01', '2019-12-30')
    Visualizer.show_distribution_log_returns(apple_portfolio)
    Visualizer.show_up_down_log_returns(apple_portfolio)





