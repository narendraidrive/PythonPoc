import unittest
from program_file.exception import RaiseExp 
class TestException(unittest.TestCase):
    def test(self):
        with self.assertRaises(Exception) as context:
            RaiseExp().valid_age(0)

        self.assertTrue('age is not valid' in str(context.exception))

    def test1(self):
        self.assertRaises(ValueError, RaiseExp().valid_age, 0)