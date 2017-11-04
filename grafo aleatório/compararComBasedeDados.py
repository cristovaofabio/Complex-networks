import networkx as nx
from numpy import *
import matplotlib.pyplot as plt

def gerarGrafo(grafo=None,arestas=None,nos=None):
	#Nesta função estou gerando uma lista adjacente de saida
	if grafo is None:
		grafo= nx.Graph() #criar um grafo nao direcionado
	if arestas is None:
		arestas=list()
	marcador=0
	Abrir = open('base_de_dados/facebook_TGF.txt','r')
	for linha in Abrir:
		vetor=linha.split() #quebrar linhas
		if(vetor[0]=="#"):
			marcador=1
		if (marcador!=1):
			numero=int(vetor[0])
			if numero not in grafo:
				grafo.add_node(numero)
		if (marcador==1 and vetor[0]!="#"):
			arestas.append(vetor)
			peso=1
			if len(vetor)==3:
				peso = int(vetor[2]) #caso tenha aresta com peso
			no1=int(vetor[0])
			no2=int(vetor[1])
			grafo.add_edge(no1, no2,weight=peso)

	Abrir.close() #fechar arquivo
	return grafo


def imprimir_grafo(grafo):
	for x in grafo:
		print(x,grafo[x])

def grafo_saida(grafo):
	soma=0
	for x in grafo:
		arest=len(grafo[x])
		#print("Grau de saida do nó %d: %d"%(x,arest))
		soma=soma+arest
	print("Quantidade de arestas:",soma/2)
	print("Quantidade media de vizinhos: %.1f"%(soma/len(grafo)))

def densidade(dic):
	aresta=0
	for chave in dic:
		aresta=aresta+len(dic[chave])
	aresta=aresta/2 #se não for direcionado
	quantNos=len(dic)
	#quantMaxima=quantNos*(quantNos-1) #se for direcionado
	quantMaxima=quantNos*(quantNos-1)/2 #se não for direcionado
	densi=(aresta/quantMaxima)
	return densi
	#print("Densidade: %.2f"%densi)

grafo = gerarGrafo()
d=densidade(grafo)

print("Para a base de dados: ")
grafo_saida(grafo)
print("Diâmetro: ",nx.diameter(grafo))

n=len(grafo) #número de nós
p=d #probabilidade de encontrar cada aresta do grafo
print(p)
grafo_aleatorio = nx.gnp_random_graph(n,p) #grafo aleatório direcionado Erdos-Rényi

print("\nPara o grafo aleatório")
grafo_saida(grafo_aleatorio)
print("Diâmetro: ",nx.diameter(grafo_aleatorio))
print(nx.is_connected(grafo_aleatorio)) #verificar se o grafo é conexo
#imprimir_grafo(grafo_aleatorio)

