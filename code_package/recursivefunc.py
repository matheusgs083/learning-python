def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")   
    elif number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

try:
    print(factorial(6))

except Exception as e:
    print(f"An error occurred: {e}")