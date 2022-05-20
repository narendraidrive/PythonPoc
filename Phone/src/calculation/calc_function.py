
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # try: 
    return a * 1.0 / b
    # except Exception as e:
    #     return e


def factorial(a):
    if(a != 1) :
        return a * factorial(a-1)
    else :
        return 1