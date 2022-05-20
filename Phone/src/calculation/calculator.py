from .calc_function import *

class Calculator(object):
    def __init__(self):
        self._answer = 0.0

    def last_answer(self):
        return self._answer

    def _do_math(self, a, b, func):
        self._answer = func(a, b)
        return self._answer

    def add(self, a, b):
        return self._do_math(a, b, add)

    def subtract(self, a, b):
        return self._do_math(a, b, subtract)

    def multiply(self, a, b):
        return self._do_math(a, b, multiply)

    def divide(self, a, b):
        return self._do_math(a, b, divide)

    def factorial(self, a):
        return factorial(a)