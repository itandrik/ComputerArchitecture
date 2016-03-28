import yaml


# Serializing data object to .yaml file
def yaml_write(file_name, data):
    with open(file_name + '.yaml', 'wt') as file:
        yaml.dump(data, file)


# Deserialization of .yaml file
def yaml_read(file_name):
    try:
        with open(file_name + '.yaml', 'rt') as file:
            return yaml.load(file)
    except OSError:
        print('Such file does not exist!')
