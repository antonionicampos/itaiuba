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

	def getSequenciaJogos(self, numeroJogos='all', asc=True):
		"""
		Retorna uma sequencia de jogos especifica, com o numero de jogos a ser extraido (numeroJogos) 
		e se sao do inicio da lista (asc=True) ou do final (asc=False)
		"""
		if numeroJogos == 'all':
			return self.jogos
		else:
			if numeroJogos > len(self.jogos):
				numeroJogos = len(self.jogos)
			lista = self.jogos
			if not asc:
				lista.reverse()
			i = 0
			jogos = []
			for jogo in lista:
				i = i + 1
				jogos.append(jogo)
				if i == numeroJogos:
					return jogos
					break

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

	def ocorrenciaDosNumeros(self, listaDeNumeros='all', percentual=False):
		"""
			Retorna um dicionario com as ocorrencias dos numeros em uma lista de numeros ou as ocorrencias
			dentro dos jogos que o compoem
		"""
		dic = {}
		if listaDeNumeros == 'all':
			listaDeNumeros = self.getNumeros()
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
		"""
		Compara a (self)Lista de Jogos com outra listaDeJogos e retorna a recorrencia dos numeros contidos nelas

		"""

		dic = {}
		for num in self.getNumeros():
			contador = 0
			for jogo in listaDeJogos.getSequenciaJogos():
				for n in jogo.getNumeros():
					if num == n:
						contador = contador + 1
			dic[num] = contador
			if percentual:
				dic[num] = (contador / float(len(listaDeJogos.getSequenciaJogos()) * 6)) * 100
		return dic

	def repeticoesPorJogosSeguidos(self, numJogosSeguidos):
		"""
		Conta quantas vezes se repetiu numeros em sequencias de jogos combinados 2 a 2... 3 a 3...(numJogosSeguidos)
		"""
		jogoSelecionado = []
		dic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
		i = 0
		for jogo in self.jogos:
			jogoSelecionado.extend(jogo.getNumeros())
			i = i + 1
			num_recorrencias = 0
			if (i == numJogosSeguidos):
				for num in list(set(jogoSelecionado)):
					contador = 0
					for n in jogoSelecionado:
						if num == n:
							contador = contador + 1
					if contador == numJogosSeguidos:
						num_recorrencias = num_recorrencias + 1
				
				dic[num_recorrencias] = dic[num_recorrencias] + 1
				del jogoSelecionado[0:6]
				i = numJogosSeguidos - 1
		return dic

	def getParesImpares(self, percentual=False):
		"""
		Retorna um dicioanrio com a quantidade ou o percentual de numeros pares e impares no grupo de jogos.
		"""
		dic = {'par' : 0, 'impar' : 0 }
		for jogo in self.jogos:
			dic['par'] = dic['par'] + jogo.getParesImpares()['par']
			dic['impar'] = dic['impar'] + jogo.getParesImpares()['impar']
		if percentual:
			dic['par'] = (dic['par'] / (len(self.jogos) * 6.0)) * 100
			dic['impar'] = (dic['impar'] / (len(self.jogos) * 6.0)) * 100
		return dic






