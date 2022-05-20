import pytest
from calculation import Calculator


def verify_answer(expected, answer, last_answer):
    assert expected == answer
    assert expected == last_answer

def test_last_answer_init():
    cal = Calculator()
    assert cal.last_answer() == 0.0

def test_add():
    cal =  Calculator()
    answer = cal.add(3, 2)
    verify_answer(5.0, answer, cal.last_answer())

def test_subtract():
    cal =  Calculator()
    answer = cal.subtract(6, 5)
    verify_answer(1.0, answer, cal.last_answer())


def test_subtract_negative():
    cal =  Calculator()
    answer = cal.subtract(5, 6)
    verify_answer(-1.0, answer, cal.last_answer())


def test_multiply():
    cal =  Calculator()
    answer = cal.multiply(10, 10)
    verify_answer(100.0, answer, cal.last_answer())


def test_divide():
    cal =  Calculator()
    answer = cal.divide(10, 2)
    verify_answer(5, answer, cal.last_answer())

# def test_divide_by_zero():
#      cal =  Calculator()
#     with pytest.raises(ZeroDivisionError) as e:
#     cal.divide(1, 0)
#     assert "division by zero" in str(e.value)

def test_factorial():
    cal =  Calculator()
    answer = cal.factorial(3)
    assert 6.0 == answer

