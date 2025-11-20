
def divide_numbers(x, y):
    try:

        result = x / y
        
        print("Result:", result)

    except ZeroDivisionError:
        
        print("The division by zero operation is not allowed.")

numerator = 100

denominator = 5

divide_numbers(numerator, denominator)