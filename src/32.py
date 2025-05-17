def find_largest_product(numbers):
    max_product = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            temp_product = 1
            for j in range(i+1, len(numbers)):
                if numbers[j] < 0:
                    break
                else:
                    temp_product *= numbers[i] * numbers[j]
                    max_product = max(max_product, temp_product)
    return max_product

# Example usage
numbers = [2, -3, -4, 5, -6]
print(find_largest_product(numbers))
