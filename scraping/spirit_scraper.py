from parsel import Selector
import requests


class SpiritScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    MAIN_URL = "https://animespirit.tv/xfsearch/%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5%20%D0%BF%D1%80%D0%BE%20%D0%B4%D0%B5%D0%BC%D0%BE%D0%BD%D0%BE%D0%B2/"
    LINK_XPATH = '//div[@class="custom-poster"]/a/@href'
    IMG_XPATH = '//div[@class="custom-poster"]/a/img/@src'
    SERIES_XPATH = '//div[@class="custom-label1"]/text()'

    def parse_data(self):
        html = requests.get(url=self.MAIN_URL, headers=self.headers,
                            proxies="http://username:password@123.43.677.89:6789").text
        # print(html)
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        images = tree.xpath(self.IMG_XPATH).extract()
        series = tree.xpath(self.SERIES_XPATH).extract()
        for link in links:
            print(link)
        for image in images:
            print(image)
        for serie in series:
            print(serie)


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.parse_data()
