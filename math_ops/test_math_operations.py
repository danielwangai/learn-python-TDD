import unittest
from math_operations import add_numbers

class MathOps(unittest.TestCase):
    def test_method_adds_correcty(self):
        self.assertEqual(add_numbers(3, 4), 7)


if __name__== '__main__':
    unittest.main()
