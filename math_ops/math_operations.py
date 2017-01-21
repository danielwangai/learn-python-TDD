def get_numbers(number_1, number_2):
    # returns list of numbers, ready for operation
    return [number_1, number_2]

def add_numbers(list_of_numbers):
    return sum(list_of_numbers)

def subtract_numbers(list_of_numbers):
    return (list_of_numbers[0] - list_of_numbers[1])

def multiply_numbers(list_of_numbers):
    return list_of_numbers[0]*list_of_numbers[1]

def divide_numbers(list_of_numbers):
    if list_of_numbers[1] == 0:
        return "Error"
    else:
        return list_of_numbers[0]/list_of_numbers[1]
