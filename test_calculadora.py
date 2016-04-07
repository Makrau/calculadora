import pytest
from calculadora import ClassCalculadora
def test_calculadora_adicao():
	calc = ClassCalculadora()
	assert calc.adicao(3,2) == 5

def test_calculadora_subtracao():
	calc = ClassCalculadora()
	assert calc.subtracao(3,2) == 1

def test_calculadora_divisao():
	calc = ClassCalculadora()
	assert calc.divisao(4,2) == 2

def test_calculadora_multiplicacao():
	calc = ClassCalculadora()
	assert calc.multiplicacao(4,2) == 8

def test_calculadora_potencia():
	calc = ClassCalculadora()
	assert calc.potencia(4,2) == 16

def test_calculadora_raiz():
	calc = ClassCalculadora()
	assert calc.raiz(4.0,2.0) == 2

def test_calculadora_log():
	calc = ClassCalculadora()
	assert calc.logaritmo(4.0, 2.0) == 2

def test_calculadora_fatorial():
	calc = ClassCalculadora()
	assert calc.fatorial(5) == 120

def test_calculadora_valor_absoluto():
	calc = ClassCalculadora()
	assert calc.valor_absoluto(-10) == 10