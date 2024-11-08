import sys
import convert

#Task 3:
#Purpose: Converts str to float and adds the nums/floats to determine sum
def main():
    total_sum = 0.0
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        number = convert.str_to_float(arg)
        if number is not None:
            total_sum += number
        i += 1
    return total_sum

if __name__ == '__main__':
    # print(sys.argv)
    main()