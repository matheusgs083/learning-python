def sum_decorator(func):
    print("Decorator is being applied")

    def wrapper(x, y):
        print("Calculating the sum...")
        result = func(x, y)
        print(f"The sum of {x} and {y} is {result}")
        return result
    return wrapper

def multiply_decorator(func):
    print("Decorator is being applied")

    def wrapper(x, y):
        print("Calculating the product...")
        result = func(x, y)
        print(f"The product of {x} and {y} is {result}")
        return result
    return wrapper

@sum_decorator # decotator is applied here.
def sum(x, y):
    return x + y

@multiply_decorator # decotator is applied here.
def multiply(x, y):
    return x * y

print(sum(10, 5))
print(multiply(10, 5))

# decorator example.
