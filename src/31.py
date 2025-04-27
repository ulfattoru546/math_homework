def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    return 3.14 * radius ** 2

if __name__ == "__main__":
    import sys
    print(f"The area of a circle with radius {sys.argv[1]} is: {calculate_area(sys.argv[1])}")
