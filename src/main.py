import scrapy
import googlemaps
from pymongo import MongoClient
from datetime import datetime

CITY_NAME = 'Cascavel'
MONGOCONECTION = 'mongodb+srv://gkannemberg:<Temporaria123>@cluster0.rnikrwi.mongodb.net/'

class ImoveisSpider(scrapy.Spider):
    name = 'imoveis'
    start_urls = ['https://www.imobiliariacidade.com.br']
    base_url = 'https://www.imobiliariacidade.com.br/venda/?&pagina={}'  # URL base com o marcador de página

    def start_requests(self):
        # Gera solicitações para cada página
        for page_number in range(1, 64):  # o site possui 64 paginas por conta disso o for passa por todas
            url = self.base_url.format(page_number)
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):
        for imovel in response.css('div.anuncio'):
            titulo = imovel.css('h2::text').get()
            preco = imovel.css('span.preco::text').get()
            localizacao = imovel.css('p.localizacao::text').get()
            
            yield {
                'titulo': titulo,
                'preco': preco,
                'localizacao': localizacao,
            }


def save_in_mongodb(parsed_response):
    client = MongoClient(MONGOCONECTION, 27017)
    db = client.scraping

    colection_imobiliarias = db['imobiliarias']
    colection_imobiliarias.insert_one(parsed_response)


def main():
    imoveis_spider = ImoveisSpider()
    response = imoveis_spider.start_requests()
    parsed_response = ImoveisSpider.parse(imoveis_spider, response)
    save_in_mongodb(parsed_response)

main()
# def scrape_data():
#     scraped_data = {}

#     scraped_data["raw_address"] = "Rua São Damião"
#     scraped_data["created_at"] = datetime.now()

#     return scraped_data


# def enrich_address(scraped_data):

#     gmaps_request_string = f"{CITY_NAME}, "

#     enriched_address = googlemaps.search(gmaps_request_string)

#     return enriched_address


# def save_address_mongo(enriched_data):

#     pymongo.save(enriched_data)
    


# def process():

#     scraped_data = scrape_data()

#     enriched_data = enrich_address(scraped_data)

#     all_data = scraped_data.update(enriched_data)

#     save_address_mongo(all_data)



#  process()



    
