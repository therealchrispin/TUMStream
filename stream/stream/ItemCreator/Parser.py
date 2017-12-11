import json
from abc import ABC, abstractmethod
from stream.ItemCreator.Validator import Validator


class Parser(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def parse(self, data_object):
        """"""

    @abstractmethod
    def get_item_value(self):
        """"""


class JSONParser(Parser):
    def __init__(self):
        Parser.__init__(self)
        self.__item_value = {}
        self.__validator = Validator()

    def parse(self, data_object):
        data = json.loads(data_object)
        if self.__validator.data_is_valid(data):
            self.__item_value = data
            self.set_object_path()
            return True

    def get_item_value(self):
        return self.__item_value

    def set_object_path(self):
        if 'object_path' not in self.__item_value.keys():
            self.__item_value['object_path'] = ""
