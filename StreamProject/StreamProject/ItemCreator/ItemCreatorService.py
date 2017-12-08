from StreamProject.ItemCreator.ItemCreator import ItemCreator
from StreamProject.ItemCreator.Parser import JSONParser


class ItemCreatorService:

    @staticmethod
    def create_item_from_json(data):
        parser = JSONParser()

        item_creator = ItemCreator()
        item_creator.set_parser(parser)
        item_creator.set_data_object(data)
        try:
            item_creator.create_item()
        except ValueError:
            return "wrong data keys"
