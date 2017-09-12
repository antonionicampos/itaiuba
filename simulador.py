from jogo import Jogo
from jogos import Jogos
from volante import Volante

class Simulador:

	def __init__(self, fileName='megasena.xlsx', qntSorteios=10, jogos=[]):
		self.historico = Jogos(fileName=fileName)
		self.simuSorteios = []
		self.simuHistorico = []
		i = 0
		self.volantes = []
		if len(jogos.getSequenciaJogos()) >=1:
			for jogo in jogos.getSequenciaJogos():
				self.volantes.append(Volante(aposta=jogo))
		for jogo in self.historico.getSequenciaJogos()[::-1]:
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

	def getVolantes(self):
		return self.volantes