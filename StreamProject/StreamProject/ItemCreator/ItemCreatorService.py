from StreamProject.StreamProject.ItemCreator.ItemCreator import ItemCreator
from StreamProject.StreamProject.ItemCreator.Parser import JSONParser


class ItemCreatorService:

    @staticmethod
    def create_item_from_json(data):
        json_parser = JSONParser()
        ItemCreator(json_parser, data)
