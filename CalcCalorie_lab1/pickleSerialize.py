import pickle


class Pickle:

    def __init__(self, file_name):
        self.file_name = file_name

    # Serializing of data to the .pickle file
    def dump(self, data):
        with open(self.file_name + '.pickle', 'wt') as f:
            pickle.dump(data, f)

    # Deserialization of data from the .pickle file
    def read(self):
        try:
            with open(self.file_name + '.pickle', 'rt') as f:
                return pickle.load(f)
        except IOError:
            print ("File doesn't exist")
