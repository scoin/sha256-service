from model import Model
from hashlib import sha256
import json


class Hash(Model):

    @staticmethod
    def encode(json_data):
        return sha256(json.dumps(json_data)).hexdigest()

    def save(self, json_data):
        hash_output = self.encode(json_data)
        return super(Hash, self).save(hash_output, json_data)
