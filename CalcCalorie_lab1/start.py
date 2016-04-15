from controller import Controller
from controller_args import ControllerArgs
import configparser


def read_config():
        try:
            parser = configparser.ConfigParser()
            parser.read('config.ini')
            return parser.get('controller_type', 'controller')
        except configparser.ParsingError:
            print ('Could not parse:')

if __name__ == '__main__':
    controller_type = read_config()
    if controller_type == 'args':
        ControllerArgs().parse()
    elif controller_type == 'menu':
        Controller().menu()
    else:
        print ('Cant start program, check controller')
