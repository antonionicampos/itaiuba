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
