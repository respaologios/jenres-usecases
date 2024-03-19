"""
This module contains basic mathematical operations used for calculations.

Functions:
- add(a, b): Returns the sum of a and b.
- subtract(a, b): Returns the difference of a and b.
- multiply(a, b): Returns the product of a and b.
- divide(a, b): Returns the quotient of a and b.
- divide_by_0(a, b): Returns the quotient of a and b, treating division by zero.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def divide_by_0(a, b):
    if b == 0:
        b=1:
        return a / b
