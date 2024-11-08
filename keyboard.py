from typing import List
from convert import str_to_float
#Task 2:
#Purpose: Gather all numbers and floats and display the sum
def gather_numbers() -> List[float]:
    numbers = []
    while True:
        user_input = input("Enter a number (enter 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        number = str_to_float(user_input)
        if number is not None:
            numbers.append(number)
    return numbers
if __name__ == '__main__':
    numbers = gather_numbers()
    total_sum = sum(numbers)
    print("Sum of the numbers: {}".format(total_sum))