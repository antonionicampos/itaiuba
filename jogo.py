class Jogo:

	def __init__(self, numeros=[], numConcurso=0):
		# numeros: os 6 numeros sorteados num dado concurso
		self.numeros = numeros
		# numConcurso: numero do concurso
		self.numConcurso = numConcurso

	def getNumeros(self):
		return self.numeros