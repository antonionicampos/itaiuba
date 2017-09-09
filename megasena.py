import lib
import matplotlib.pyplot as plt
from sets import Set


jogos = lib.extrairJogosPlanilha()
previsao_jogos = lib.extrairJogosPlanilha('ultimosjogos.xlsx') #Abre o arquivo q contem os ultimos 10 jgos para validar o algoritmo
per_acerto = []
qnt_sugeridos = []
total_sugeridos = []
qnt_acertos_fibo = []
qnt_sugeridos_fibo = []
n = 1 #variavel para simulacao.. Indica o jogo da planilha "ultimosjogos.xlsx" a ser considerado como o jogo mais recente
num_mais_ocorrencias = 3
num_menos_ocorrencias = 5
for n in range (1, 10):
	if n >= (len(previsao_jogos) / 6):
		n = (len(previsao_jogos) / 6) - 1 #protecao para o n ser no maximo a penultima linha do arquivo "ultimosjogos"
	if n>1:
		for i in range(0, n * 6):
			jogos.append(previsao_jogos[i]) #extende a lista jogos 
	valores_per = lib.contarOcorrencias(jogos, lib.getNumeros())
	valores_per_ordenados, percentuais_ordenados = lib.ocorrenciasOrdenadas(valores_per, jogos)
	mais_ocorrencias = []
	menos_ocorrencias = []
	for element in list(valores_per_ordenados[0:num_mais_ocorrencias]):
		mais_ocorrencias.append(int (element))
	for element in list(valores_per_ordenados[-num_menos_ocorrencias:]):
		menos_ocorrencias.append(int (element) )

	print('Os numeros que mais sairam: ')
	print(mais_ocorrencias)
	print('Os numeros que menos sairam: ')
	print (menos_ocorrencias)

	#print('Qntd de numeros que se repetiram em dois jogos seguidos em toda a Historia: ')
	num_repetiram_por_jogos = lib.repeticoesPorJogosSeguidos(jogos, 2)
	total_numeros_repetidos = lib.totalNumerosRepetidos(num_repetiram_por_jogos)
	#print(total_numeros_repetidos)

	######################################################################################################################################
	#tentando gerar uma lista com numeros sugeridos para acertar pelo menos um numero

	ultimos_jogos = lib.listaDosUltimosJogos(jogos, 4) #lista os 4 ultimos jogos do arquivo que tem todo o historico de resultados
	num_repetiram_por_jogos = lib.repeticoesPorJogosSeguidos(ultimos_jogos, 2) #Conta numeros que se repetiram de 2 em 2 jogos
	total_numeros_repetidos = lib.totalNumerosRepetidos(num_repetiram_por_jogos) #Organiza a resposta num dicionario
	#plt.plot(list(total_numeros_repetidos.keys()), list(total_numeros_repetidos.values())) #plota o resultado
	valores_per = lib.contarOcorrencias(ultimos_jogos, lib.getNumeros()) #conta as recorrencias dos numeros nos 4 ultimos jogos
	valores_per_ordenados, percentuais_ordenados = lib.ocorrenciasOrdenadas(valores_per, ultimos_jogos) #ordena elas em uma tupla


	numeroDeJogos = lib.numeroDeJogos(previsao_jogos) #Conta qnts jogos tem no arquivo
	suposto_ultimo_jogo = lib.jogo(previsao_jogos, n) #Pega o jogo do arquivo "ultimosjogos" para teste como se fosse o ultimo resultado

	lista = list(Set(ultimos_jogos) & Set(lib.getNumeros())) #Cria uma lista apenas com os numeros que sairam nos ultimos 4 resultados
	primeira_sugestao = list(Set(lista) - Set(suposto_ultimo_jogo)) #remove os numeros o ultimo jogo (visto q eh dificil repetir numeros)
	conta_ocorrencias_numSugeridos = lib.contarOcorrencias(jogos, primeira_sugestao)
	print ('Primeiros - Numeros sugeridos: ')
	print (primeira_sugestao) #Imprime a primeiro lista de numeros sugeridos
	maisEmenos_ocorrencias = []
	maisEmenos_ocorrencias.extend(mais_ocorrencias)
	maisEmenos_ocorrencias.extend(menos_ocorrencias)
	sugeridos_ordenados, per_ordenados = lib.ocorrenciasOrdenadas(conta_ocorrencias_numSugeridos, jogos)
	#print (sugeridos_ordenados, conta_ocorrencias_numSugeridos) #Imprime o numero de ocorrencia historica dos numSugeridos
	numeros_sugeridos = []
	for num in range(len(sugeridos_ordenados)):
		if per_ordenados[num] < 1.72: #Observei que saem mais os numeros que tem o percentual de ocorrencias inferior a esse valor
			numeros_sugeridos.append(int(sugeridos_ordenados[num]))

	numeros_sugeridos.extend(maisEmenos_ocorrencias)
	numeros_sugeridos = list(Set(numeros_sugeridos))
	numeros_sorteados = lib.jogo(previsao_jogos, n+1)#Pega o jogo seguinte do arq "ultimosjogos" como se fosse o numero sorteado
	print ('Numeros sugeridos: ')
	print (numeros_sugeridos) #Imprime a lista de numeros sugeridos
	
	print ('Numeros "sorteados": ')
	print (numeros_sorteados) #imprime os numeros do suposto sorteio

	print ('Num comum ..entre a primeira sugestao e sorteado: ')
	print (Set(primeira_sugestao) & Set(numeros_sorteados)) #separa os numeros que estavam na lista de sugestao q foram sorteados

	print ('Num comum ..entre a numeros sugeridos e sorteado: ')
	res = Set(numeros_sugeridos) & Set(numeros_sorteados)
	print (res) #separa os numeros que estavam na lista de sugestao q foram sorteados

	print ('Qnt de numeros sugeridos: ')
	print (len(numeros_sugeridos))

	print ('Qnt de acertos: ')
	per_acerto.append(len(res))
	print (per_acerto[n-1])
	qnt_sugeridos.append(len(numeros_sugeridos))
	fibo = []
	for sugeridos in numeros_sugeridos:
		fibo.extend(lib.getFibonacci(sugeridos))
	numeros_sugeridos.extend(fibo)
	numeros_sugeridos = Set(numeros_sugeridos)
	print (numeros_sugeridos)
	
	res = Set(numeros_sugeridos) & Set(numeros_sorteados)
	qnt_acertos_fibo.append(len(res))
	qnt_sugeridos_fibo.append(len(numeros_sugeridos))

	print ('----------------------------------------------------------------------')

	######################################################################################################################################

plt.bar(range(1, len(per_acerto)+1), qnt_sugeridos, width=0.7,color='red')
plt.bar(range(1, len(per_acerto)+1), per_acerto, width=0.5,color='green')
plt.bar(range(1, len(per_acerto)+1), qnt_sugeridos_fibo, width=0.3,color='purple')
plt.bar(range(1, len(per_acerto)+1), qnt_acertos_fibo, width=0.1,color='yellow')

sena = []
for i in  range(0, len(per_acerto)):
	sena.append(6)
quina = []
for i in  range(0, len(per_acerto)):
	quina.append(5)
quadra = []
for i in  range(0, len(per_acerto)):
	quadra.append(4)
plt.plot(range(1, len(per_acerto)+1),sena)
plt.plot(range(1, len(per_acerto)+1),quina)
plt.plot(range(1, len(per_acerto)+1),quadra)
plt.show()#Mostra todos os graficos que foram plotados ao longo do programa
print(lib.getFibonacci(2))

