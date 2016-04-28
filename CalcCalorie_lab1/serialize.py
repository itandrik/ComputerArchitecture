import configparser
from pickleSerialize import Pickle
from jsonSerialize import Json
from yamlSerialize import Yaml
import global_koefs

class Serialize:

    def __init__(self):
        self.parser = configparser.ConfigParser()

    @staticmethod
    def change_config(serialization_type, filename):
        cfgfile = open("config.ini", 'w')
        config = configparser.ConfigParser()
        # add the settings to the structure of the file, and lets write it out
        if not config.has_section('serialization'):
            config.add_section('serialization')
        config.set('serialization', 'name', serialization_type)
        config.set('serialization', 'filename', filename)
        config.write(cfgfile)
        cfgfile.close()

    def read_config(self):
        try:
            self.parser.read('config.ini')
            return self.parser.get('serialization', 'name'),\
                self.parser.get('serialization', 'filename')
        except configparser.ParsingError:
            print ('Could not parse:')

    def load(self):
        serial = self.read_config()
        temp = []
        try:
            if serial[0] == 'pickle':
                temp = Pickle(serial[1]).read()
            elif serial[0] == "json":
                temp = Json(serial[1]).read()
            elif serial[0] == "yaml":
                temp = Yaml(serial[1]).read()
            if temp[0] == 1:
                gender = 'male'
            else:
                gender = 'female'
            print ('Gender : %s; Weight : %dkg; Height : %dsm;\n'
                   ' Age : %d; Physical activity : %s; Calories : %f' %
                  (gender, temp[1], temp[2],
                   temp[3], global_koefs.str2[temp[4]], temp[5]))
        except TypeError:
            print ("No such file")

    def dump(self, data):
        serial = self.read_config()
        if serial[0] == 'pickle':
            return Pickle(serial[1]).dump(data)
        elif serial[0] == "json":
            return Json(serial[1]).dump(data)
        elif serial[0] == "yaml":
            return Yaml(serial[1]).dump(data)
