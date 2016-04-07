import math
class ClassCalculadora():
	def adicao(self, x, y):
		resultado = x + y

		return resultado

	def subtracao(self, x, y):
		resultado = x - y

		return resultado

	def divisao(self, x, y):
		resultado = x / y

		return resultado

	def multiplicacao(self, x, y):
		resultado = x * y

		return resultado

	def potencia(self, x, y):
		resultado = x ** y

		return resultado

	def raiz(self, x, y):
		resultado = x ** (1/y)

		return resultado

	def logaritmo(self, x, y):
		resultado = math.log(x, y)

		return resultado

	def fatorial(self, x):
		if(x <= 1):
			return 1
		else:
			return x * self.fatorial(x-1)

	def valor_absoluto(self, x):
		pass