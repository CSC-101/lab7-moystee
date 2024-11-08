from typing import Optional

#Task 1:
#Converts string input to float output
def str_to_float(s: str) -> Optional[float]:
    try:
        return float(s)
    except ValueError:
        return None
if __name__ == '__main__':
    numbers = str_to_float()
    total_sum = sum(numbers)
