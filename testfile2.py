import main
import unittest


class TestScript(unittest.TestCase):

    def testFour(self):
        pass

    def test_0(self):
        # it should return an object
        self.assertIsInstance(
            main.countWords("ask a bunch try a bunch get a bunch"),
            dict,
            msg='should return a dict')

    def test_1(self):
        # it should return an object where each property gives a word in the
        # string, with its number of appearances
        result = {'ask': 1, 'a': 2, 'bunch': 2, 'get': 1}
        self.assertEqual(
            main.countWords("ask a bunch get a bunch"),
            result,
            msg='should return a dict where each key gives a word in the string, with the value its number of appearances')

    def test_2(self):
        # it should return an empty dict if passed an empty string
        self.assertEqual(
            main.countWords(""),
            {},
            msg='should return an empty dict if passed an empty string')
