import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quote = response.css("span.text::text").get()
        author = response.css("span small.author::text").get()

        yield {
            "quote": quote,
            "author": author,
        }
