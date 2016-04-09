class Model(object):
    def __init__(self):
        self.data = {}

    def get(self, key, default=None):
        return self.data.get(key, default)

    def save(self, key, value):
        self.data[key] = value
        return key
