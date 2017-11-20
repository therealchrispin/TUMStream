class Stream:
    def __init__(self):
        self.__streamItems = []

    def set_stream_items(self, streamItemList):
        self.__streamItems = streamItemList

    def add_stream_item(self, streamItem):
        self.__streamItems.append(streamItem)

    def get_stream_items(self):
        return self.__streamItems