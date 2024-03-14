# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# import config_database
import pymongo


class ImobiliariasPipeline():
    
    # Initialize the MongoDB pipeline with your database and collection names
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    # Open the MongoDB connection in the open_spider method
    @classmethod
    def from_crawler(cls, crawler):
        # Get the MongoDB connection information from the settings
        mongo_uri = crawler.settings.get('MONGO_URI')
        mongo_db = crawler.settings.get('MONGO_DB')
        mongo_collection = crawler.settings.get('MONGO_COLLECTION')

        # Initialize the pipeline with the MongoDB connection information
        return cls(mongo_uri, mongo_db, mongo_collection)

    # Connect to the MongoDB database and collection in the open_spider method
    def open_spider(self, spider):
        # Create a connection to the MongoDB server
        self.client = MongoClient(self.mongo_uri)

        # Get a reference to the database and collection
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    # Save the scraped data to the MongoDB database and collection in the process_item method
    def process_item(self, item, spider):
        # Insert the item into the MongoDB collection
        self.collection.insert_one(dict(item))

        # Return the item for further processing
        return item
