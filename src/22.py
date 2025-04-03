def square_sum(numbers):
    """Calculate the sum of squares of given numbers"""
    return sum(x**2 for x in numbers)

numbers = [1, 2, 3]
result = square_sum(numbers)
print(result)  # Output: 14 (1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14)
