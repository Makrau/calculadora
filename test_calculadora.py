import pytest
from calculadora import ClassCalculadora
def test_calculadora_adicao():
	calc = ClassCalculadora()
	assert calc.adicao(3,2) == 5
