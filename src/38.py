import math
sqrt = lambda x: math.sqrt(x)
max_len = 50

def find_sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = int(num % 10)
        sum += digit
        num //= 10
    return sum

def main():
    n = input("Enter a number: ")
    if len(n) < max_len:
        print("Please enter at least", max_len, "digits.")
    else:
        num_str = str(int(n))
        for i in range(len(num_str), -1, -1):
            digit = int(num_str[i])
            sum_of_digits = find_sum_of_digits(digit)
            if 3 <= sum_of_digits < 20:
                print("Number:", n, "Sum of digits:", sum_of_digits)
                break

if __name__ == "__main__":
    main()
