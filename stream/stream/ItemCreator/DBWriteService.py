from stream.models.StreamItemModel import StreamItemModel


class DBWriteService:

    @staticmethod
    def save_item_in_db(request, item_dict):

        item = StreamItemModel(
            title=item_dict['title'],
            description=item_dict['description'],
            topic=item_dict['topic'],
            category=item_dict['category'],
            object_path=item_dict['object_path']
        )

        request.dbsession.add(item)
