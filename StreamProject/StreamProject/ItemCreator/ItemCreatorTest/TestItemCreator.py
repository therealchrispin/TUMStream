import unittest
from StreamProject.StreamProject.ItemCreator.ItemCreator import ItemCreator
from StreamProject.StreamProject.ItemCreator.ItemCreatorService import ItemCreatorService
from StreamProject.StreamProject.ItemCreator.Parser import JSONParser
from StreamProject.StreamProject.StreamItem import StreamItem


class TestItemCreation(unittest.TestCase):
    def setUp(self):
        self.item_creator = ItemCreator()

    def testItemCreationWithFalseJSON(self):
        test_json = {
                    'title': 'testItem',
                    'description': 'this is just a test item',
                    'topic': 'topic',
                    'category': 'cat'}

        json_parser = JSONParser()
        self.item_creator.set_parser(json_parser)
        self.item_creator.set_data_object(test_json)

        try:
            self.item_creator.create_item()
        except ValueError:
            pass

        item = self.item_creator.get_stream_item()
        self.assertIsNone(item)

    def testItemCreationWithCorrectJSON(self):
        test_json = {
                    'ID': '1',
                    'title': 'test',
                    'description': 'test with correct Json',
                    'category': 'cat',
                    'topic':' topic',
                    'object_path': 'no_path'
        }

        json_parser = JSONParser()
        self.item_creator.set_parser(json_parser)
        self.item_creator.set_data_object(test_json)

        self.item_creator.create_item()

        item = self.item_creator.get_stream_item()
        self.assertIsInstance(item, StreamItem)

    def testItemCreatorServiceWithFalseJSON(self):
        test_json = {
                    'title': 'testItem',
                    'description': 'thisisjustatestimtem',
                    'topic': 'topic',
                    'category': 'cat'}
        response = ItemCreatorService.create_item_from_json(test_json)
        self.assertEqual(response, "wrong data keys")



