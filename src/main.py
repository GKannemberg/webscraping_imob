import scrapy
import googlemaps
import pymongo
from datetime import datetime

CITY_NAME = 'Cascavel'

def scrape_data():
    scraped_data = {}

    scraped_data["raw_address"] = "Rua São Damião"
    scraped_data["created_at"] = datetime.now()

    return scraped_data


def enrich_address(scraped_data):

    gmaps_request_string = f"{CITY_NAME}, "

    enriched_address = googlemaps.search(gmaps_request_string)

    return enriched_address


def save_address_mongo(enriched_data):

    pymongo.save(enriched_data)
    


def process():

    scraped_data = scrape_data()

    enriched_data = enrich_address(scraped_data)

    all_data = scraped_data.update(enriched_data)

    save_address_mongo(all_data)



# process()

    
