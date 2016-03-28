import unittest
import StringIO


class TestUM(unittest.TestCase):
    def testStrings(self):
        outp = StringIO.StringIO()
        self.assertEqual(outp.readline(), '')

if __name__=='main':
    unittest.main()
