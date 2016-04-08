import yaml


class Yaml:

    def __init__(self, file_name):
        self.file_name = file_name

    # Serializing data object to .yaml file
    def dump(self, data):
        with open(self.file_name + '.yaml', 'wt') as f:
            yaml.dump(data, f)

    # Deserialization of .yaml file
    def read(self):
        try:
            with open(self.file_name + '.yaml', 'rt') as f:
                return yaml.load(f)
        except IOError:
            print('Such file does not exist!')
