# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

title_translation = {
    "Apartamento Padrão": {"category": "apartment", "sub_category": "standard"},
    "Casa Padrão": {"category": "apartment", "sub_category": "standard"},
    "Comercial Edificio Co...": {"category": "apartment", "sub_category": "standard"},
    "Terreno Lote Urbano": {"category": "apartment", "sub_category": "standard"},
    "Rural Sítio": {"category": "apartment", "sub_category": "standard"},
}


class ImobiliariasPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        standartize_title(adapter)

        normalize_price(adapter)

        items["title"] = title
        items["price"] = price
        items["bairro"] = bairro

        return item


def standartize_title(adapter):
    title_string = adapter.get("title")
    dict_translation = title_translation[title_string]

    adapter["category"] = dict_translation["category"]
    adapter["sub_category"] = dict_translation["sub_category"]


def normalize_price(adapter):
    price_string = adapter.get("price")

    price_int = int(price_string.split(",")[0].replace(".", ""))
    adapter["price"] = price_int
