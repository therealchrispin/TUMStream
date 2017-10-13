
class StreamItem:
    def __init__(self, category="", topic=""):
        self.__ID = ""
        self.__title = ""
        self.__description = ""
        self.__category = category
        self.__topic = topic
        self.__object_path = ""

    def set_id(self, id):
        self.__ID = id

    def get_id(self):
        return self.__ID

    def get_object_path(self):
        return self.__object_path

    def set_object_path(self, object_path):
        self.__object_path = object_path

    def get_objects(self):
        return self.__object_path

    def get_topic(self):
        return self.__topic

    def get_category(self):
        return self.__category

    def set_topic(self, topic):
        self.__topic = topic

    def set_category(self, category):
        self.__category = category

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description
