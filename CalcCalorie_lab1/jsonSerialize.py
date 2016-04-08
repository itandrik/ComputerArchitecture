import json


class Json:

    def __init__(self, file_name):
        self.file_name = file_name

    # Serializing data object to .json file
    def dump(self, data):
        with open(self.file_name + '.json', 'wt') as f:
            json.dump(data, f)

    # Deserialization of .json file
    def read(self):
        try:
            with open(self.file_name + '.json', 'rt') as f:
                return json.load(f)
        except IOError:
            print "File doesn't exist"
