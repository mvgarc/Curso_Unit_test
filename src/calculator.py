def sum(a,b):
    """
    >>> sum(5,7)
    12

    >>> sum(5,5)
    10
    """
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """
    >>> divide (10, 0)
    """
    if b == 0:
        raise ValueError("La division por cero no esta permitida")
    return a / b