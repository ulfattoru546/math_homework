import random

def find_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: A list of numerical values (integers or floats).
        
    Returns:
        The average value of the input list.
    """
    return sum(numbers) / len(numbers)

# Generate some sample data
sample_data = [1, 2, 3, 4, 5]
average_value = find_average(sample_data)
print("The average is:", average_value)
