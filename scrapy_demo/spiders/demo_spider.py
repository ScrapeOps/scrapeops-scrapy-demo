import scrapy
from scrapy_demo.items import QuoteItem

class DemoSpider(scrapy.Spider):
    name = 'demo_spider'
    allowed_domains = ['quotes.toscrape.com']

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            'http://quotes.toscrape.com/page/3/',
            'http://quotes.toscrape.com/page/4/',
            'http://quotes.toscrape.com/page/5/',
            'http://quotes.toscrape.com/page/6/',
            'http://quotes.toscrape.com/page/7/',
            'http://quotes.toscrape.com/page/8/',
            'http://quotes.toscrape.com/page/9/',
            'http://quotes.toscrape.com/page/10/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item
