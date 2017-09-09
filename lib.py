from openpyxl import load_workbook
import itertools
from sets import Set

def getNumeros():
	return list(range(1, 61))

def contarNumero(jogos, numero):
	contador = 0
	for valor in jogos:
		if(valor == numero):
			contador = contador + 1
	return contador
def getFibonacci(numero=1):
	"""
	Retorna a sequencia de fibonacci para o numero de entrada
	Para a sequencia quando valores extrapolam 60
	Por padrao numero = 1 que retorna a sequencia pura
	"""
	f=[]
	f.append(1*numero)
	f.append(f[0])
	for i in range(2, 10):
		fibbo = f[i-1] + f[i-2]
		if fibbo > 60:
			break
		f.append(fibbo)
	return f
def extrairJogosPlanilha(filename='megasena.xlsx'):
	"""
	Extrai todos os jogos da planilha da Megasena.xlsx
	Parametros:
		filename - Nome do arquivo da planilha .xlsx
	Retorna:
		jogos - Lista com todos os jogos da Megasena (ex: [1, 32, 13, 33, 41, 5, ...])
	"""
	wb = load_workbook(filename)
	ws = wb.active
	jogos = []
	for lin in ws.rows:
		if (lin[2].value is not None) and (lin[0].value <> 'Concurso'):
			jogo = [int(lin[2].value), int(lin[3].value), int(lin[4].value),
					int(lin[5].value), int(lin[6].value), int(lin[7].value)]
			jogos.extend(jogo)

	return jogos

def contarOcorrencias(jogos, numeros):
	"""
	Calcula o percentual de ocorrencia de cada numero da Megasena
	Parametros:
		jogos - Lista com todos os jogos da Megasena (ex: [1, 32, 13, 33, 41, 5, ...])
	Retorna:
		valores_per - Dicionario com cada numero da Megasena (string) com seu respectivo percentual (float)
		(Ex.: {'1': 1.453456, '2': 1.783241, ...})
	"""
	tamanho_jogos = float(len(jogos))
	valores_per = {}

	for num in numeros:
		contar_ocorrencia = contarNumero(jogos, num)
		valores_per[str(num)] = ((contar_ocorrencia / tamanho_jogos) * 100.0)

	return valores_per

def ocorrenciasOrdenadas(valores_per, jogos):
	"""
	
	"""
	tamanho_jogos = float(len(jogos))
	valores_per_ordenados = sorted(valores_per, key=valores_per.get, reverse=True)
	percentuais_ordenados = []
	for item in valores_per_ordenados:
		ocorr = contarNumero(jogos, int(item))
		percentuais_ordenados.append(valores_per[item])
		print('{:2}: {:.4f}% -> Numero de Ocorrencias: {:d} / {:d}'.format(item, valores_per[item], ocorr, int(tamanho_jogos)))

	return valores_per_ordenados, percentuais_ordenados

def jogo(jogos, numDoConcurso):
	return jogos[(6*(numDoConcurso-1)):(6*(numDoConcurso-1)+6)]

def repeticoesPorJogosSeguidos(jogos, numJogosSeguidos):
	repeticoes_numeros_jogos = []
	qnt_de_jogos_geral = int (len(jogos) / 6)
	for num_jogo in range(numJogosSeguidos, qnt_de_jogos_geral + 1):
		jogosSelecionados = []
		jogosSelecionados2 = []
		for num_do_jogo in range(0, numJogosSeguidos):
			jogosSelecionados.extend(jogo(jogos, num_jogo - num_do_jogo))
		for num_do_jogo in range(0, numJogosSeguidos):
			jogosSelecionados2.append(jogo(jogos, num_jogo - num_do_jogo))
		
		res = Set(jogosSelecionados)
		
		for jogoi in jogosSelecionados2:
			res = res & Set(jogoi)
		repeticoes_numeros_jogos.append(len(res))
	return repeticoes_numeros_jogos

def totalNumerosRepetidos(numRepetidos):
	"""
	Quantidade de numeros repetidos em uma sequencia de 2 jogos
	"""
	total_numeros_repetidos = {}
	for quantidade in range(0, 7):
		contador = 0
		for num in numRepetidos:
			if quantidade == num:
				contador = contador + 1
		total_numeros_repetidos[quantidade] = contador
	return total_numeros_repetidos

def listaDosUltimosJogos(jogos, qnt):
	ultimo_concurso = int(len(jogos) / 6)
	ultimosJogos = []
	for num_jogo in range(0, qnt):
		ultimosJogos.extend(jogo(jogos, ultimo_concurso - num_jogo))
	return ultimosJogos

def numeroDeJogos(jogos):
	return len(jogos)/6
