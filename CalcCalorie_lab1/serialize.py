import ConfigParser
from pickleSerialize import Pickle
from jsonSerialize import Json
from yamlSerialize import Yaml
import view


class Serialize:

    def __init__(self):
        self.parser = ConfigParser.SafeConfigParser()

    @staticmethod
    def change_config(serialization_type, filename):
        cfgfile = open("config.ini", 'w')
        config = ConfigParser.ConfigParser()
        # add the settings to the structure of the file, and lets write it out...
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
        except ConfigParser.ParsingError, err:
            print 'Could not parse:', err

    def make_pretty_output(self, fn):
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

    @make_pretty_output
    def load(self):
        serial = self.read_config()
        if serial[0] == 'pickle':
            return Pickle(serial[1]).read()
        elif serial[0] == "json":
            return Json(serial[1]).read()
        elif serial[0] == "yaml":
            return Yaml(serial[1]).read()

    def dump(self, data):
        serial = self.read_config()
        if serial[0] == 'pickle':
            return Pickle(serial[1]).dump(data)
        elif serial[0] == "json":
            return Json(serial[1]).dump(data)
        elif serial[0] == "yaml":
            return Yaml(serial[1]).dump(data)
