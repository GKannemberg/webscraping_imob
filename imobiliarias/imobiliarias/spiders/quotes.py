import scrapy
from imobiliarias.items import ImobiliariasItem

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://www.imobiliariaativa.com.br/pesquisa-de-imoveis/"]
  

    def parse(self, response):
        imoveis = response.css("#property-listing .col-lg-3")
        items = ImobiliariasItem()
        
        for imovel in imoveis:
            title = imovel.css("div h3 a::text").get(),
            price = imovel.css("div.price span::text").get(),
            bairro = imovel.css("h3 small::text").get(),
            
            items['title'] = title
            items['price'] = price
            items['bairro'] = bairro
            
            yield items
                
            
        
        next_page = response.xpath('//li[9]/a/@href').get()  
        
        if next_page is not None:
            next_page_url = "https://www.imobiliariaativa.com.br" + next_page
            yield scrapy.Request(response.urljoin(next_page_url))
            
            
            
            #yield response.follow(next_page_url, callback= self.parse), another method for turn pages.


    
        
        