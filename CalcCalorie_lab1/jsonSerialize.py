import json


# Serializing data object to .json file
def json_write(file_name, data):
    with open(file_name + '.json', 'wt') as file:
        json.dump(data, file)


# Deserialization of .json file
def json_read(file_name):
    try:
        with open(file_name + '.json', 'rt') as file:
            return json.load(file)
    except OSError:
        print('Such file does not exist!')
