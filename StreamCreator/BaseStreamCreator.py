from abc import ABC, abstractmethod

from StreamCreator.Stream import Stream


class BaseStreamCreator(ABC):
    def __init__(self):
        self.__streamItems = []
        self.__stream = Stream()

    def __getStreamItems(self, *args):
        pass

    def getStream(self):
        self.__createStream()
        return self.__stream

    @abstractmethod
    def __createStream(self):
        pass
