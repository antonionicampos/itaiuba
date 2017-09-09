from jogo import Jogo
from openpyxl import load_workbook

class Jogos:

	def __init__(self, listaJogos=[], filename=''):
		if filename != '': 
			self.jogos = self.extrairJogosPlanilha(filename)
		else:
			self.jogos = listaJogos


	def getNumeros(self):
		listaNum = []
		for jogo in self.jogos:
			listaNum.extend(jogo.getNumeros())
		return list(set(listaNum))

	def getJogos(self):
		return self.jogos

	def extrairJogosPlanilha(self, filename):
		"""
		Extrai todos os jogos de uma planilha excel (formato da megasena.xlsx)
		Parametros:
			filename - Nome do arquivo da planilha .xlsx
		Retorna:
			jogos - Lista com todos os jogos da Megasena (ex: [[1, 32, 13, 33, 41, 5], ...])
		"""
		wb = load_workbook(filename)
		ws = wb.active
		jogos = []

		for lin in ws.rows:
			if (lin[2].value is not None) and (lin[0].value != 'Concurso'):
				jogo = Jogo()
				jogo.numeros = [int(lin[2].value), int(lin[3].value), int(lin[4].value),
								int(lin[5].value), int(lin[6].value), int(lin[7].value)]
				jogo.numConcurso = int(lin[0].value)
				jogos.append(jogo)

		return jogos

	def ocorrenciaDosNumeros(self, listaDeNumeros, percentual=False):
		dic = {}
		for num in listaDeNumeros:
			contador = 0
			for jogo in self.jogos:
				for n in jogo.getNumeros():
					if n == num:
						contador = contador + 1
			if not percentual:
				dic[num] = contador
			else:
				dic[num] = (contador / float(len(listaDeNumeros))) * 100
		return dic

	def ocorrenciaDosNumerosNumaListaDeJogos(self, listaDeJogos, percentual=False):
		dic = {}
		for num in self.getNumeros():
			contador = 0
			for jogo in listaDeJogos.getJogos():
				for n in jogo.getNumeros():
					if num == n:
						contador = contador + 1
			dic[num] = contador
			if percentual:
				dic[num] = (contador / float(len(listaDeJogos.getJogos()) * 6)) * 100
		return dic

