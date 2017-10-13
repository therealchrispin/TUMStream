from SQLiteDataBase import DB
from StreamItem import StreamItem


class ItemCreator:
    def __init__(self, parser, data_object):
        self.__parser = parser
        self.__data_object = data_object
        self.__Item = {}
        self._parse_data_object()

    def _parse_data_object(self):
        self.__parser.parse(self.__data_object)
        self.__Item = self.__parser.getItemValues()

    def create_item(self):
        stream_item = StreamItem()

        stream_item.set_title(self.__Item['title'])
        stream_item.set_description(self.__Item['description'])
        stream_item.set_topic(self.__Item['topic'])
        stream_item.set_category(self.__Item['category'])

        self.__save_item(stream_item)

    @staticmethod
    def __save_item(stream_item):
        database = DB()
        database.insertData(
            (
             stream_item.get_title(),
             stream_item.get_description(),
             stream_item.get_topic(),
             stream_item.get_category(),
             stream_item.get_object_path()
            )
        )

