import unittest
import convert

class TestCases(unittest.TestCase):
    def test_str_translate_1(self):
        input = 'Rishub'
        expected = None
        result = convert.str_to_float(input)
        self.assertEqual(expected, result)
