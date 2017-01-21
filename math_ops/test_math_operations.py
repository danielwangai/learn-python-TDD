import unittest
from math_operations import add_numbers

class MathOps(unittest.TestCase):
    def test_method_adds_correcty(self):
        self.assertEqual(add_numbers(3, 4), 7)

    def test_add_non_number_params(self):
        with self.assertRaises(TypeError):
            add_numbers("2",2)
        with self.assertRaises(TypeError):
            add_numbers(2,"2")


if __name__== '__main__':
    unittest.main()
