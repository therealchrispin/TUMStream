class Stream:
    def __init__(self):
        self.__streamItems = []

    def setStreamItems(self, streamItemList):
        self.__streamItems = streamItemList

    def addStreamItem(self, streamItem):
        self.__streamItems.append(streamItem)

    def getStreamItems(self):
        return self.__streamItems