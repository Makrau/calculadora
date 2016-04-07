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

