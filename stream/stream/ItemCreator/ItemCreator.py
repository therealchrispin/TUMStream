from stream.ItemCreator.DBWriteService import DBWriteService


class ItemCreator:
    def __init__(self, request):
        self.__parser = None
        self.__data_object = None
        self.__Item = {}
        self.__request = request

    def set_parser(self, parser):
        self.__parser = parser

    def set_data_object(self, data_object):
        self.__data_object = data_object

    def _parse_data_object(self):
        if self.__parser.parse(self.__data_object):
            return True

    def __create(self):
        DBWriteService.save_item_in_db(self.__request, self.__Item)

    def create_item(self):
        try:
            if self._parse_data_object():
                self.__Item = self.__parser.get_item_value()
                self.__create()
            else:
                raise ValueError
        except ValueError:
            raise ValueError
