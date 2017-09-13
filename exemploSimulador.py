from simulador import Simulador
from jogo import Jogo
from jogos import Jogos


Aposta1 = Jogo(numeros=[1,2,3,4,5,6])
Aposta2 = Jogo(numeros=[1,2,3,4,5,6,7])

Apostas = Jogos(listaJogos=[Aposta1, Aposta2])
simulacao = Simulador(apostas=Apostas)

def att():
	#Aqui entra os codigos para atualizar as apostas para simulacao
	simulacao.setApostas(Apostas)

print('Ultimo jogo da lista de jogos a serem "sorteados": ')
print(simulacao.getSorteios().getListaJogos()[-1])
print('Ultimo jogo da lista considerada como banco de dados - historico: ')
print(simulacao.getHistorico().getListaJogos()[-1])

print('Aposta 1: ')
print(simulacao.getVolantes()[0].getAposta().getNumeros())
print('Valor R$ {:.2f}'.format(simulacao.getVolantes()[0].getPreco()))

print('Aposta 2: ')
print(simulacao.getVolantes()[1].getAposta().getNumeros())
print('Valor R$ {:.2f}'.format(simulacao.getVolantes()[1].getPreco()))

simulacao.update(func=att)

print('Ultimo jogo da lista de jogos a serem "sorteados": ')
print(simulacao.getSorteios().getListaJogos()[-1])
print('Ultimo jogo da lista considerada como banco de dados - historico: ')
print(simulacao.getHistorico().getListaJogos()[-1])
