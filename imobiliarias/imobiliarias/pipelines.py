# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# import config_database
import pymongo


class ImobiliariasPipeline():
    
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['imob_ativa']
        self.collection = db['imob_tb']         
        
    def process_item(self, item, spider):
        
        self.collection.insert_many(dict(item))
        return item

    # def store_db(self, item):
    #     self.cur.execute(
    #         """
    #         INSERT INTO real_estate_ativa
    #             (price,
    #             neighborhood,
    #             type,
    #             rooms,
    #             suites,
    #             bathrooms,
    #             garages,
    #             total_area,
    #             private_area)
    #             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    #         """,
    #         (
    #             item["price"][0],
    #             item["neighborhood"][0],
    #             item["type"][0],
    #             item["rooms"][0],
    #             item["suites"][0],
    #             item["bathrooms"][0],
    #             item["garages"][0],
    #             item["total_area"][0],
    #             item["private_area"][0],
    #         ),
    #     )
    #     self.conn.commit()

