import ConfigParser
import pickleSerialize

parser = ConfigParser.SafeConfigParser()

def change_config(type, filename):
    #if parser.has_section('serialization'):
     #   parser.remove_section('serialization')
    parser.remove_option('serialization', 'name')
    parser.set('serialization', 'name', type)
    parser.remove_option('serialization', 'filename')
    parser.set('serialization', 'filename', filename)

    parser.write('config.ini')


def read_config():
    try:
        parser = ConfigParser.SafeConfigParser()
        parser.read('config.ini')
        return parser.get('serialization', 'name'),parser.get('serialization', 'filename')
    except ConfigParser.ParsingError, err:
        print 'Could not parse:', err


def load():
    serial = read_config()
    if serial[0] == 'pickle':
