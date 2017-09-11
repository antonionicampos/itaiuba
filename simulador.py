from jogos import Jogos
from volante import Volante

class Simulador:

	def __init__(self, fileName='megasena.xlsx', qntSorteios='10'):
		self.historico = Jogos(fileName=fileName)
		self.simuSorteios = []
		self.simuHistorico = []
		self.
		i = 0
		for jogo in self.historico[::-1]:
			i = i + 1
			if i <= qntSorteios:
				self.simuSorteios.append(jogo)
			else:
				self.simuHistorico.append(jogo)
		self.simuSorteios = Jogos(listaJogos=self.simuSorteios)
		self.simuHistorico = Jogos(listaJogos=self.simuHistorico)

	def getSorteios(self):
		return self.simuSorteios

	def getHistorico(self):
		return self.simuHistorico