import pykkaimport requestsimport pandas as pdfrom bs4 import BeautifulSoupfrom abstract.crawler import AbstractCrawlerclass YahooFinanceCrawler(AbstractCrawler, pykka.ThreadingActor):    def crawl(self, symbol, url, path):        response = requests.get(url)        # need to write original html content???        soup = BeautifulSoup(response.text, 'html.parser')        columns = []        data_sheets = []        time_period = []        for breakdown in soup.find_all('div', class_="D(tbhg)"):            for divs in breakdown.find_all('div', class_="D(tbr)"):                for div in divs:                    time_period.append(div.get_text())        columns.append(time_period[0])        time_period = time_period[1:]        for datatable in soup.find_all('div', class_="D(tbrg)"):            for divs in datatable.find_all('div', class_="D(tbr)"):                data_sheet = []                column_index = 0                for div in divs:                    if column_index == 0:                        columns.append(div.get_text())                        column_index += 1                        continue                    data_sheet.append(div.get_text())                data_sheets.append(data_sheet)        data_sheets = [list(i) for i in zip(*data_sheets)]        for i, time in enumerate(time_period):            data_sheets[i].insert(0, time)        df = pd.DataFrame(data_sheets, columns=columns)        return df