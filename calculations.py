import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    logging.debug(f'Adding {a} + {b}')
    return a + b

def subtract(a, b):
    logging.debug(f'Subtracting {a} - {b}')
    return a - b

def multiply(a, b):
    logging.debug(f'Multiplying {a} * {b}')
    return a * b

def divide(a, b):
    logging.debug(f'Dividing {a} by {b}')
    if b == 0:
        logging.error('Attempted to divide by zero')
        raise ValueError("Cannot divide by zero.")
    return a / b

def divide_by_0(a, b):
    if b == 0:
        logging.warning('Divisor was 0, defaulting to 1')
        b = 1
    logging.debug(f'Dividing {a} by {b}')
    return a / b
