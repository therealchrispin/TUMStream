from abc import ABC, abstractmethod

from StreamProject.StreamCreator.Stream import Stream


class BaseStreamCreator(ABC):
    def __init__(self):
        self.__streamItems = []
        self.__stream = Stream()

    def __get_stream_items(self, *args):
        pass

    def get_stream(self):
        self.__create_stream()
        return self.__stream

    @abstractmethod
    def __create_stream(self):
        pass
