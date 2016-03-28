import pickle


# Serializing of data to the .pickle file
def pickle_dump(filename, data):
    with open(filename + '.pickle', 'wt') as f:
        pickle.dump(data, f)


# Deserialization of data from the .pickle file
def pickle_load(filename):
    try:
        with open(filename + '.pickle', 'rt') as f:
            return pickle.load(f)
    except OSError:
        print "File doesn't exist"
