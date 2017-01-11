from urllib.parse import urlparse
from scrapy.http import Request
import scrapy

class LaurelSpider(scrapy.Spider):
    name = "laurel"

    allowed_domains = [
        "www.cityoflaurel.org",
        "files.cityoflaurel.org",
        "dat.maryland.gov"
    ]

    start_urls = [
      "https://www.cityoflaurel.org/services/"
    ]

    def parse(self, response):
        base_url = 'https://www.cityoflaurel.org'
        for service in response.css('div.views-field-title'):
            service_link = service.css('a').xpath('@href').extract()[0]
            yield Request(url=base_url + service_link + '/', callback=self.second_pass)
            # yield { 'url': base_url + service_link + '/'
            # }


    def second_pass(self, response):
        base_url = 'https://www.cityoflaurel.org'
        for link in response.css('div#site-main')[0].css('a').xpath('@href').extract():
            if link.endswith('.pdf'):
                link = urlparse.urljoin(base_url, link)
                yield Request(url=link, callback=self.save_pdf)
            if "http" not in str(link):
                yield Request(url=base_url + link + '/', callback=self.third_pass)
            elif "cityoflaurel" in link:
                yield Request(url=link, callback=self.third_pass)

    def third_pass(self, response):
        base_url = 'https://www.cityoflaurel.org'
        for link in response.css('div#site-main')[0].css('a').xpath('@href').extract():
            if link.endswith('.pdf'):
                yield Request(url=link, callback=self.save_pdf)
            if "http" not in str(link):
                yield { base_url + link + '/' }
            elif "cityoflaurel" in link:
                yield { link }


    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        with open(path, 'wb') as f:
            f.write(response.body)
            f.close()
