from calculadora import calculadora

def test_adicao():
    assert calculadora(5, 3, '+') == 8

def test_subtracao():
    assert calculadora(5, 3, '-') == 2

def test_multiplicacao():
    assert calculadora(5, 3, '*') == 15

def test_divisao():
    assert calculadora(6, 3, '/') == 2

def test_divisao_por_zero():
    assert calculadora(6, 0, '/') == "Erro! Divisão por zero."
