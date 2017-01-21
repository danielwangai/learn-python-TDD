import unittest
from math_operations import add_numbers, get_numbers

class MathOps(unittest.TestCase):

    def setUp(self):
        self.list_of_numbers = get_numbers(2,3)
        self.list_num_string = get_numbers(2,"3")
        self.list_string_num = get_numbers("2",3)
        self.list_all_string = get_numbers("2","3")
    def test_method_adds_correcty(self):
        self.assertEqual(add_numbers(self.list_of_numbers), 5)

    def test_add_non_number_params(self):
        with self.assertRaises(TypeError):
            add_numbers(self.list_num_string)
        with self.assertRaises(TypeError):
            add_numbers(self.list_string_num)

    def test_data_type_of_input_is_int_or_float(self):
        # tests that both inputs are of type float or int
        type_number_1 = type(self.list_of_numbers[0]) == int or type(self.list_of_numbers[0]) == float
        type_number_2 = type(self.list_of_numbers[1]) == int or type(self.list_of_numbers[1]) == float
        self.assertTrue(type_number_1 and type_number_2)

    def test_data_type_of_atleast_one_input_not_int_or_float(self):
        # tests at least one of the inputs is of type int or float
        type_number_1 = type(self.list_num_string[0]) == int or type(self.list_num_string[0]) == float
        type_number_2 = type(self.list_num_string[1]) == int or type(self.list_num_string[1]) == float
        self.assertFalse(type_number_1 and type_number_2)

    def test_data_type_of_both_inputs_are_not_int_or_float(self):
        # tests at least one of inputs are of type int or float
        type_number_1 = type(self.list_all_string[0]) == int or type(self.list_all_string[0]) == float
        type_number_2 = type(self.list_all_string[1]) == int or type(self.list_all_string[1]) == float
        self.assertFalse(type_number_1 and type_number_2)


if __name__== '__main__':
    unittest.main()
