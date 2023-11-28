# example_module.py

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def concatenate_strings(s1, s2):
    return s1 + s2

def find_maximum(lst):
    if not lst:
        raise ValueError("Empty list")
    return max(lst)

def square_root(n):
    if n < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return n ** 0.5
