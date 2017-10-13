from StreamItem import StreamItem


class Validator:
    def __init__(self):
        self.__sample_keys = {}
        self.__set_sample_keys()

    def data_is_valid(self, data):
        sample_set = set(self.__sample_keys.keys())
        data_set = set(data.keys())
        if data_set == sample_set:
            return True
        else:
            return False

    def __set_sample_keys(self):
        class_name = StreamItem.__name__
        for key in StreamItem().__dict__.keys():
            new_key = key.replace('_'+class_name+'__', '')
            print(new_key)
            self.__sample_keys[new_key] = ""
