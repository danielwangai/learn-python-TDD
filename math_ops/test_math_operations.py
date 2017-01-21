import unittest
from math_operations import add_numbers, get_numbers

class MathOps(unittest.TestCase):

    def setUp(self):
        self.list_of_numbers = get_numbers(2,3)
        self.list_num_string = get_numbers(2,"3")
        self.list_string_num = get_numbers("2",3)
    def test_method_adds_correcty(self):
        self.assertEqual(add_numbers(self.list_of_numbers), 5)

    def test_add_non_number_params(self):
        with self.assertRaises(TypeError):
            add_numbers(self.list_num_string)
        with self.assertRaises(TypeError):
            add_numbers(self.list_string_num)


if __name__== '__main__':
    unittest.main()
