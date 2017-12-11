

class Validator:
    def __init__(self):
        self.__sample_keys = ['title', 'description', 'topic', 'category']

    def data_is_valid(self, data):
        data_set = []
        for key in data.keys():
            data_set.append(key)

        if data_set == self.__sample_keys:
            return True
        else:
            return False
