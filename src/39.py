def calculate_square_sum(n):
    """
    Calculate the sum of squares of numbers from 1 to n.
    
    Example usage:
    >>> calculate_square_sum(5)
    55
    """
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

# Check function with the provided test case
def check_solution():
    assert calculate_square_sum(5) == 55, "Test case failed"
    print("Test passed!")

check_solution()
