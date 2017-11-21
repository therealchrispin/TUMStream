import json
from abc import ABC, abstractmethod
from StreamProject.StreamProject.ItemCreator.StreamValidator import Validator


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
        if self.__validator.data_is_valid(data_object):
            self.__item_value = data_object
            return True

    def get_item_value(self):
        return self.__item_value
