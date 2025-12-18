def square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    
    return number ** 0.5

def calculate_average(numbers):
    if not numbers:
        return 0
    
    total = sum(numbers)
    return total / len(numbers)
