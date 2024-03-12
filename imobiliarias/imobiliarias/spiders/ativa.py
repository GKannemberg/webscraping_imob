import scrapy
from unidecode import unidecode

from ..items import ImobiliariasItem

amenities = ["bedrooms", "bathrooms", "garages"]


class ImobiliariaAtiva(scrapy.Spider):
    name = "ativa"
    start_urls = ["https://www.imobiliariaativa.com.br/pesquisa-de-imoveis/"]

    def parse(self, response):
        imoveis = response.css("#property-listing .col-lg-3")
        item = ImobiliariasItem()

        for imovel in imoveis:
            title = imovel.css("div h3 a::text").get()
            price = imovel.css("div.price span::text").get()
            neighborhood = imovel.css("h3 small::text").get()

            allotment_area = imovel.css("ul.imo-itens li small::text").get()

            bedrooms = imovel.css("ul.imo-itens li:first-child::text").get()
            bathrooms = imovel.css("ul > li:nth-child(2)::text").get()
            garages = imovel.css("ul > li:nth-child(3)::text").get()

            if allotment_area:
                item["allotment_area"] = allotment_area

            if bedrooms:
                item["bedrooms"] = bedrooms

            if bathrooms:
                item["bathrooms"] = allotment_area

            if garages:
                item["garages"] = garages

            item["title"] = title
            item["price"] = price
            item["neighborhood"] = neighborhood

            yield self.normalize_data(self, item)

        next_page = response.xpath("//li[9]/a/@href").get()

        if next_page is not None:
            next_page_url = "https://www.imobiliariaativa.com.br" + next_page
            yield scrapy.Request(response.urljoin(next_page_url))

            # yield response.follow(next_page_url, callback= self.parse), another method for turn pages.
