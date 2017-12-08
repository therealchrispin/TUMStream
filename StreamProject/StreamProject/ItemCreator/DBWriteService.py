from StreamProject.DbModel.models import DBSession, StreamItem


class DBWriteService:

    @staticmethod
    def save_item_in_db(item_dict):
        item = StreamItem(
            title=item_dict['title'],
            description=item_dict['description'],
            topic=item_dict['topic'],
            category=item_dict['category'],
            object_path=item_dict['object_path']
        )

        DBSession.add(item)
