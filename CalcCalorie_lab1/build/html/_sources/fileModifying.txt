import unittest
import pickleSerialize
import jsonSerialize
import yamlSerialize
from io import StringIO


# class for testing pickle module
class TestPickle(unittest.TestCase):
    def test(self):
        # dumping data into pickle file
        pickleSerialize.pickle_dump('test_pickle',
                                    (1, 72, 185, 25, 4, 32432.543))
        str = unicode('(I1\nI72\nI185\nI25\nI4\nF32432.543\ntp0\n.')
        outp = StringIO()
        with open('test_pickle.pickle', 'rt') as f:
            outp.write(unicode(f.read()))
        # verifying for right writing data into the file
        self.assertEqual(outp.getvalue(), str)


# class for testing json module
class TestJson(unittest.TestCase):
    def test(self):
        # dumping data into json file
        jsonSerialize.json_dump('test_json',
                                (2, 52, 176, 19, 3, 23623.234))
        str = unicode('[2, 52, 176, 19, 3, 23623.234]')
        outp = StringIO()
        with open('test_json.json', 'rt') as f:
            outp.write(unicode(f.read()))
        # verifying for right writing data into the file
        self.assertEqual(outp.getvalue(), str)


# class for testing yaml module
class TestYaml(unittest.TestCase):
    def test(self):
        # dumping data into json file
        yamlSerialize.yaml_write('test_yaml',
                                (2, 52, 176, 19, 3, 2013.2277749999998))
        str = unicode('!!python/tuple '
                      '[2, 52, 176, 19, 3, 2013.2277749999998]\n')
        outp = StringIO()
        with open('test_yaml.yaml', 'rt') as f:
            outp.write(unicode(f.read()))
        # verifying for right writing data into the file
        self.assertEqual(outp.getvalue(), str)

if __name__ == '__main__':
    unittest.main()
