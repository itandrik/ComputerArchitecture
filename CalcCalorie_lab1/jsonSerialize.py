import json


# Serializing data object to .json file
def json_dump(file_name, data):
    with open(file_name + '.json', 'wt') as file:
        json.dump(data, file)


# Deserialization of .json file
def json_read(file_name):
    try:
        with open(file_name + '.json', 'rt') as f:
            objs = []
            while 1:
                try:
                    objs.append(json.load(f))
                except EOFError:
                    return objs

    except IOError:
        print "File doesn't exist"
