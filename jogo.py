class Jogo:

	def __init__(self, numeros=[], numConcurso=0):
		# numeros: os 6 numeros sorteados num dado concurso
		self.numeros = numeros
		# numConcurso: numero do concurso
		self.numConcurso = numConcurso

	def getNumeros(self):
		return self.numeros

	def getQuadrante(self):
		"""
		Funcao retorna em que quadrante do volante o numero se encontra
		"""
		quadrante = []
		for numero in self.numeros:
			if (numero > 0) and (numero <= 5):
				quadrante.append(1)
			elif(numero <= 9):
				quadrante.append(2)
			numeroStr = str(numero)
			if len(numeroStr) > 1:
				if (numero <= 30 ):
					if (int(numeroStr[1]) < 6) and (int(numeroStr[1]) != 0):
						quadrante.append(1)
					else:
						quadrante.append(2)
				if (numero <= 60 ) and (numero > 30 ):
					if (int(numeroStr[1]) < 6) and (int(numeroStr[1]) != 0):
						quadrante.append(3)
					else:
						quadrante.append(4)
		return quadrante
	def getParesImpares(self, percentual=False):
		par = 0
		impar = 0
		for num in self.getNumeros():
				if num % 2 == 0:
					par = par + 1
				else:
					impar = impar + 1
		if percentual:
			par = (par / 6.0) * 100
			impar = (impar / 6.0) * 100
		dic = {'par': par, 'impar': impar}
		return dic