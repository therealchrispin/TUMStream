
from StreamProject.StreamProject.StreamItem import StreamItem


class ItemCreator:
    def __init__(self):
        self.__parser = None
        self.__data_object = None
        self.__stream_item = None
        self.__Item = {}

    def set_parser(self, parser):
        self.__parser = parser

    def set_data_object(self, data_object):
        self.__data_object = data_object

    def _parse_data_object(self):
        if self.__parser.parse(self.__data_object):
            return True

    def __create(self):
        self.__stream_item = StreamItem()

        self.__stream_item.set_id(self.__Item['ID'])
        self.__stream_item.set_title(self.__Item['title'])
        self.__stream_item.set_description(self.__Item['description'])
        self.__stream_item.set_topic(self.__Item['topic'])
        self.__stream_item.set_category(self.__Item['category'])
        self.__stream_item.set_object_path(self.__Item['object_path'])

        self.__save_item(self.__stream_item)

    def create_item(self):
        try:
            if self._parse_data_object():
                self.__Item = self.__parser.get_item_value()
                self.__create()
            else:
                raise ValueError
        except ValueError:
            raise ValueError

    def get_stream_item(self):
        return self.__stream_item

    @staticmethod
    def __save_item(stream_item):
        """"""""


