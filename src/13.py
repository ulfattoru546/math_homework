def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given integer.
    
    Args:
    n: An integer to find the largest prime factor of
    
    Returns:
    The largest prime factor of n
    """
    i = 2
    while i * i <= n:
        if n % (i * i):
            return i
        else:
            i += 1
    return n

# Example usage
n = 60
print(f"The largest prime factor of {n} is: {find_largest_prime_factor(n)}")
