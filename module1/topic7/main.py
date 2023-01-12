"""
   Name: Deon Daigh
   Date: 01/12/2023
   Module 1 Topic 7 Assignment
"""

def divide(x, y):
    return x / y

def wrapper(func):
    def inner(x, y):
        if y == 0:
            print("You can't divide by zero!")
        else:
            return func(x * 2, y * 3)
    return inner

@wrapper
def divide(x, y):
    return x / y

print(divide(12, 2))

