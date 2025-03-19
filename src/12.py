def solve_quadratic(a, b, c):
    """Solves a quadratic equation of the form ax^2 + bx + c = 0.
    
    Args:
        a (int): Coefficient of x^2
        b (int): Coefficient of x
        c (int): Constant term
        
    Returns:
        list[float]: The two solutions to the equation
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    else:
        solution1 = (-b + sqrt(discriminant)) / (2*a)
        solution2 = (-b - sqrt(discriminant)) / (2*a)
        return [solution1, solution2]
