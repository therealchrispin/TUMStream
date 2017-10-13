import json
from abc import ABC, abstractmethod
from ItemCreator.StreamValidator import Validator


class Parser(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def parse(self, data_object):
        pass

    @abstractmethod
    def get_item_value(self):
        pass


class JSONParser(Parser):
    def __init__(self):
        Parser.__init__(self)
        self.__item_value = {}
        self.__validator = Validator()

    def parse(self, data_object):
        data = json.loads(data_object)
        if self.__validator.data_is_valid(data):
            self.__item_value = data

    def get_item_value(self):
        return self.__item_value
