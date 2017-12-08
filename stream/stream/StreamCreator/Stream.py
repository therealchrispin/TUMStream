from stream.StreamCreator.StreamConverter import StreamConverter
from stream.StreamCreator.StreamItem import StreamItem
from stream.models.StreamItemModel import StreamItemModel


class Stream:
    def __init__(self, request):
        self.__streamItems = []
        self.request = request

    def get_all(self):
        item_list = self.request.dbsession.query(StreamItemModel).all()

        for item in item_list:
            stream_item = StreamItem()
            stream_item.set_id(item.id)
            stream_item.set_title(item.title)
            stream_item.set_description(item.description)
            stream_item.set_category(item.category)
            stream_item.set_topic(item.topic)
            stream_item.set_object_path(item.object_path)
            self.__streamItems.append(
                stream_item.__dict__()
            )

        return self.__streamItems
