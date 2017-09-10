class volante:

	def __init__(self, aposta=''):
		self.numeros = list(range(1,61))
		self.aposta = aposta

	def getNumeros(self):
		return self.numeros

	def getAposta(self):
		return self.aposta

	def getPreco(self):
		dic = {6:	3.5,7: 24.5, 8:	98,9: 294, 10:	735, 11: 1617.00, 12: 3234.00, 13: 6006.00, 14:	10510.50, 15: 17517.50}
		return dic[len(self.aposta)]


	def getNumerosBordaVolante(self):
		numeros = list(range(1,11))
		numeros.extend([11,21,31,41,20,30,40,50])
		numeros.extend(range(51,61))
		numeros = list(set(numeros))
		return numeros

	def getNumerosCentroVolante(self):
		numeros = list(range(1,60))
		numeros = list(set(numeros) - set(getNumerosBordaVolante()))
		return numeros

	def getQuadrante(self, jogo):
		"""
		Funcao retorna em que quadrante do volante o numero se encontra
		"""
		quadrante = []
		numeros = jogo.getNumeros()
		for numero in numeros:
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