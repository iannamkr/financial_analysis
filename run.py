
from utils import FileUtils
from config.config import Config


def make_technical_analysis_portfolio(symbols):
    from portfolio.TechnicalAnalysisPortfolio import TechnicalAnalysisPortfolio

    portfolio = TechnicalAnalysisPortfolio(config, symbols)

    from portfolio.visualizer import Visualizer

    apple_portfolio = portfolio.get_portfolio('AAPL')

    Visualizer.show_moving_average(apple_portfolio, '2019-01-01', '2019-12-30')
    Visualizer.show_distribution_log_returns(apple_portfolio)
    Visualizer.show_up_down_log_returns(apple_portfolio)


def fetch_tickers(symbols):
    from fetcher.YahooFinanceFetcher import YahooFinanceFetcher

    fetcher = YahooFinanceFetcher(config)
    tickers = fetcher.fetch_all(symbols)

    # file cache if need visualize charts
    for symbol in symbols:
        FileUtils.save_file(tickers[symbol], config.fetchedTicker, symbol)


def crawling_financials(symbols):
    import pykka
    from crawler.YahooFinanceFrontier import YahooFinanceFrontier
    from crawler.YahooFinanceCrawler import YahooFinanceCrawler

    frontier = YahooFinanceFrontier(config, symbols)
    robots = frontier.get_robots()

    pool_size = 5 if len(symbols) > 5 else len(symbols)
    resolvers = [YahooFinanceCrawler.start().proxy() for _ in range(pool_size)]

    crawlers = []
    for i, symbol in enumerate(symbols):
        url = config.financials.format(symbol)
        path = config.crawledFinancials
        robot = robots[symbol]
        if robot.can_fetch("*", url):
            crawlers.append(resolvers[i % len(resolvers)].crawl(symbol, url, path))

    crawled_results = dict(zip(symbols, pykka.get_all(crawlers)))

    # file cache if need visualize charts
    for symbol in symbols:
        FileUtils.save_file(crawled_results[symbol], config.crawledFinancials, symbol)

    pykka.ActorRegistry.stop_all()


if __name__ == '__main__':
    config = Config()

    # fetch_tickers(['IBM', 'GOOG', 'MSFT', 'AAPL', 'INTC'])
    crawling_financials(['IBM', 'GOOG', 'MSFT', 'AAPL', 'INTC'])

    make_technical_analysis_portfolio(['IBM', 'GOOG', 'MSFT', 'AAPL', 'INTC'])
