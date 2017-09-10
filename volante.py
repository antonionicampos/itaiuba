class volante:

	def __init__(self):
		self.numeros = list(range(1,61))

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