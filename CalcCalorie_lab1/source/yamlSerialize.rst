import yaml


# Serializing data object to .yaml file
def yaml_write(file_name, data):
    with open(file_name + '.yaml', 'wt') as file:
        yaml.dump(data, file)


# Deserialization of .yaml file
def yaml_read(file_name):
    try:
        with open(file_name + '.yaml', 'rt') as f:
            objs = []
            while 1:
                try:
                    objs.append(yaml.load(f))
                except EOFError:
                    return objs
    except IOError:
        print('Such file does not exist!')
