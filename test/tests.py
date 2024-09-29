from calculadora import *

def test_calculadora_soma():
    assert calculadora(1, 1, '+') == 2
    

def test_calculadora_sub():
    assert calculadora(3, 2, '-') == 1


def test_calculadora_multiplicacao():
    assert calculadora(5, 5, '*') == 25


def test_calculadora_divisao():
    assert calculadora(10, 2, '/') == 5