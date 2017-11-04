import networkx as nx
from numpy import *
import matplotlib.pyplot as plt

def imprimir_grafo(grafo):
	for x in grafo:
		print(x,grafo[x])

def varias_probabilidades(n):
	quant=100 
	p=0.01
	valoresP=dict()
	eixoX=list()
	eixoY=list()
	while(p<=0.1):
		eixoX.append(p)
		soma=0
		for x in range(quant):
			grafo_aleatorio = nx.gnp_random_graph(n,p)
			if (nx.is_connected(grafo_aleatorio)):
				soma=soma+1
		eixoY.append(soma)
		valoresP[p]=soma
		p=p+0.01
	legenda="Para %d nós"%n
	plt.plot(eixoX, eixoY,label=legenda)
	plt.xlabel("Probabilidade de encontrar uma aresta")
	plt.ylabel("Porcentagem")
	plt.legend()

quantNos=50
valores=dict()
while (quantNos<=200):
	print("\nCálculo para %d nos..."%quantNos)
	varias_probabilidades(quantNos)
	quantNos=quantNos+50

#imprimir_grafo(valores)

plt.show()
#grafico(valores)
