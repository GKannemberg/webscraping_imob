# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImobiliariasItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    # type = scrapy.Field()
    bedrooms = scrapy.Field()
    neighborhood = scrapy.Field()
    allotment_area = scrapy.Field()
    # suites = scrapy.Field()
    bathrooms = scrapy.Field()
    garages = scrapy.Field()
    # private_area = scrapy.Field()
    # total_area = scrapy.Field()
