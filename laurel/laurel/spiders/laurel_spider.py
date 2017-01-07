from urllib.parse import urlparse
import scrapy

class LaurelSpider(scrapy.Spider):
    name = "laurel"

    allowed_domains = ["www.cityoflaurel.org"]
    start_urls = [
      "https://www.cityoflaurel.org/services/"
    ]

    def parse(self, response):
        base_url = 'https://www.cityoflaurel.org'
        for service in response.css('div.field-departments'):
            service_link = service.css('a').xpath('@href').extract()[0]
            yield {
              'url': base_url + service_link
            }

    #     for a in response.xpath('//a[@href]/@href'):
    #         link = a.extract()
    #         if link.endswith('.pdf'):
    #             link = urlparse.urljoin(base_url, link)
    #             yield http.Request(link, callback=self.save_pdf)
    #
    # def save_pdf(self, response):
    #     path = response.url.split('/')[-1]
    #     with open(path, 'wb') as f:
    #         f.write(response.body)
