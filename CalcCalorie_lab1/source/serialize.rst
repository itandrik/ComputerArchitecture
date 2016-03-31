import ConfigParser
import pickleSerialize
import jsonSerialize
import yamlSerialize
import view
parser = ConfigParser.SafeConfigParser()


def change_config(type, filename):
    cfgfile = open("config.ini", 'w')
    config = ConfigParser.ConfigParser()
    # add the settings to the structure of the file, and lets write it out...
    if not config.has_section('serialization'):
        config.add_section('serialization')
    config.set('serialization', 'name', type)
    config.set('serialization', 'filename', filename)
    config.write(cfgfile)
    cfgfile.close()


def read_config():
    try:
        parser = ConfigParser.SafeConfigParser()
        parser.read('config.ini')
        return parser.get('serialization', 'name'),\
            parser.get('serialization', 'filename')
    except ConfigParser.ParsingError, err:
        print 'Could not parse:', err


def makePrettyOutput(fn):
    def wrapped():
        iterator = 1
        try:
            for i in fn():
                if i[0] == 1:
                    gender = 'male'
                else:
                    gender = 'female'
                print '%d. Gender : %s; Weight : %dkg; Height : %dsm;\n' \
                      ' Age : %d; Physical activity : %s; Calories : %f' %\
                      (iterator, gender, i[1], i[2],
                       i[3], view.str2[i[4]], i[5])
                iterator += 1
                print '\n'
        except TypeError:
            print "No file! You must dump smth"
    return wrapped


@makePrettyOutput
def load():
    serial = read_config()
    if serial[0] == 'pickle':
        return pickleSerialize.pickle_load(serial[1])
    elif serial[0] == "json":
        return jsonSerialize.json_read(serial[1])
    elif serial[0] == "yaml":
        return yamlSerialize.yaml_read(serial[1])


def dump(data):
    serial = read_config()
    if serial[0] == 'pickle':
        return pickleSerialize.pickle_dump(serial[1], data)
    elif serial[0] == "json":
        return jsonSerialize.json_dump(serial[1], data)
    elif serial[0] == "yaml":
        return yamlSerialize.yaml_write(serial[1], data)
