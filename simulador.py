from jogo import Jogo
from jogos import Jogos
from volante import Volante
import matplotlib.pyplot as plt

class Simulador:

	def __init__(self, fileName='megasena.xlsx', qntSorteios=10, apostas=[]):
		self.historico = Jogos(fileName=fileName)
		self.simuSorteios = []
		self.simuHistorico = []
		i = 0
		self.volantes = []
		if len(apostas.getSequenciaJogos()) >=1:
			for jogo in apostas.getSequenciaJogos():
				self.volantes.append(Volante(aposta=jogo))
		for jogo in self.historico.getSequenciaJogos():
			i = i + 1
			if i >= (len(self.historico.getSequenciaJogos()) - qntSorteios):
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

	def update(self, func=None):
		tamanho_sorteios = len(self.simuSorteios.getSequenciaJogos())
		if tamanho_sorteios > 1:
			self.simuHistorico.addJogo(self.simuSorteios.getSequenciaJogos()[tamanho_sorteios-1])
			self.simuSorteios.removeJogo(tamanho_sorteios-1)
		if func is not None:
			func()


