import unittest
import pickleSerialize
import jsonSerialize
import yamlSerialize


# class for testing pickle module
class TestPickle(unittest.TestCase):
    def test(self):
        # dumping data into pickle file
        obj = (1, 72, 185, 25, 4, 32432.543)
        pickleSerialize.pickle_dump('test_pickle',
                                    obj)
        obj_deserialize = pickleSerialize.pickle_load('test_pickle')
        self.assertEqual(obj, obj_deserialize[0])


# class for testing json module
class TestJson(unittest.TestCase):
    def test(self):
        # dumping data into json file
        obj = [2, 52, 176, 19, 3, 23623.234]
        jsonSerialize.json_dump('test_json',
                                obj)
        obj_deserialize = jsonSerialize.json_read('test_json')
        self.assertEqual(obj,obj_deserialize)


# class for testing yaml module
class TestYaml(unittest.TestCase):
    def test(self):
        # dumping data into json file
        obj = [2, 52, 176, 19, 3, 2013.2277749999998]
        yamlSerialize.yaml_write('test_yaml',
                                obj)
        obj_deserialize = yamlSerialize.yaml_read('test_yaml')
        self.assertEqual(obj,obj_deserialize)

if __name__ == '__main__':
    unittest.main()
