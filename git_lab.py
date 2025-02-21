import math

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract_numbers(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply_numbers(a, b):
    """Returns the product of two numbers."""
    return a / b

def add_positive_numbers(a):
    """Rteruns the sum of all positive numbers in the list a"""
    return sum(x for x in a if x > 0)
