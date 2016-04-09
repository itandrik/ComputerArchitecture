from controller import Controller
from controller_args import ControllerArgs
import ConfigParser


def read_config():
        try:
            parser = ConfigParser.SafeConfigParser()
            parser.read('config.ini')
            return parser.get('controller_type', 'controller')
        except ConfigParser.ParsingError, err:
            print 'Could not parse:', err

if __name__ == '__main__':
    controller_type = read_config()
    if controller_type == 'args':
        ControllerArgs().parse()
    elif controller_type == 'menu':
        Controller().menu()
    else:
        print 'Cant start program, check controller'
