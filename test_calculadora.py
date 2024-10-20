from calculadora import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(3, 2) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(5, 2) == 3
    assert restar(0, 0) == 0

def test_multiplicar():
    assert multiplicar(3, 2) == 6
    assert multiplicar(0, 100) == 0

def test_dividir():
    assert dividir(6, 2) == 3
    assert dividir(5, 0) == "Error: División por cero"
