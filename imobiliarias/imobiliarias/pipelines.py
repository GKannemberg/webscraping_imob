# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo

class ImobiliariasPipeline():
    
    
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    
    @classmethod
    def from_crawler(cls, crawler):
        
        mongo_uri = crawler.settings.get('MONGO_URI')
        mongo_db = crawler.settings.get('MONGO_DB')
        mongo_collection = crawler.settings.get('MONGO_COLLECTION')

        
        return cls(mongo_uri, mongo_db, mongo_collection)

   
    def open_spider(self, spider):
        
        self.client = MongoClient(self.mongo_uri)

       
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    
    def process_item(self, item, spider):
        
        self.collection.insert_one(dict(item))

        return item
