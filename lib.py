import itertools
from sets import Set


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
		fibo = f[i-1] + f[i-2]
		if fibo > 60:
			break
		f.append(fibo)
	return f

def getNumerosBordaVolante():
	numeros = list(range(1,11))
	numeros.extend([11,21,31,41,20,30,40,50])
	numeros.extend(range(51,61))
	numeros = list(set(numeros))
	return numeros

def getNumerosCentroVolante():
	numeros = list(range(1,60))
	numeros = list(set(numeros) - set(getNumerosBordaVolante()))
	return numeros
