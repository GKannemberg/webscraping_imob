# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# import config_database
from unidecode import unidecode


class ImobiliariasPipeline():
    pass
    # def __init__(self):

    #     self.DB_HOST = "localhost"  #'127.0.0.1'
    #     self.DB_NAME = "postgres"
    #     self.DB_USER = "postgres"
    #     self.DB_PASS = "postgres"

    #     self.create_connection()
    #     self.create_table()

    # def create_connection(self):
    #     self.conn = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS, host=self.DB_HOST)
    #     self.cur = self.conn.cursor()

    # def process_item(self, item, spider):
    #     self.normalize_data(item)
    #     self.store_db(item)
    #     return item

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

    def normalize_data(self, item):
        self.normalize_title(item)

        self.normalize_price(item)

        self.normalize_bairro(item)

    def normalize_title(self, item):
        title_string = item.get("title")

        item["title"] = unidecode(title_string.lower())

    def normalize_price(self, item):
        price_string = item.get("price")

        if "\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t" in price_string:
            price_string = price_string.replace("\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t", "")

        if "\t\t\t\t\t\t\t\t\t\t\t\t\t\t" in price_string:
            price_string = price_string.replace("\t\t\t\t\t\t\t\t\t\t\t\t\t\t", "")

        item["price"] = float(price_string.split(",")[0].replace(".", ""))

    def normalize_bairro(self, item):
        bairro_string = item.get("bairro")

        item["bairro"] = str(bairro_string.split(" ")[0].replace("Bairro:", ""))
