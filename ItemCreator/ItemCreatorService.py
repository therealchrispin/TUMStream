from ItemCreator.Parser import *
from ItemCreator.ItemCreator import ItemCreator


class ItemCreatorService:

    @staticmethod
    def create_item_from_json(data):
        json_parser = JSONParser()
        ItemCreator(json_parser, data)
