import networkx as nx
import matplotlib.pyplot as plt
from collections import OrderedDict

def percorrer_dicionario(dicionario,n,m):
	eixoX=list()
	eixoY=list()
	dicionario =OrderedDict(sorted(dicionario.items(), key=lambda t: t[0])) #ordenar o dicionario
	for x in dicionario:
		eixoX.append(x)
		eixoY.append(dicionario[x])
		#print(x,dicionario[x])

	legenda="Para n=%d m=%d"%(n,m)
	plt.plot(eixoX, eixoY,label=legenda)
	plt.xlabel("Graus")
	plt.ylabel("Quantidade")
	plt.legend()

def grafo_saida(grafo,n,m):
	#soma=0
	graus=dict()
	for x in grafo:
		arest=len(grafo[x])

		if (arest not in graus):
			graus[arest]=1
		else:
			graus[arest]=graus[arest]+1

		#print("Grau de saida do nó %d: %d"%(x,arest))
		#soma=soma+arest
	#print("Diâmetro: ",nx.diameter(grafo))
	percorrer_dicionario(graus,n,m) #dicionario com a frequência de cada grau

	#print("Quantidade de arestas:",soma/2)
	#print("Quantidade media de vizinhos: %.1f"%(soma/len(grafo)))

def densidade(n,grafo):
	max_aresta= (n*(n-1))/2
	soma=0
	for x in grafo:
		soma=soma+len(grafo[x])

	aresta_encontradas=soma/2

	if (max_aresta==0):
		print("Quantidade máxima de arestas: 0")
	else:
		densidade=aresta_encontradas/max_aresta
		print("Densidade encontrada: %.2f"%densidade)

#n=5
#m=4 #numero de arestas a serem adicionadas aleatoriamente a cada nó
p=0 #probabilidade de adionar um triângulo

'''for m in range(1,11):
	for n in range((m+1),11):
		grafo=nx.powerlaw_cluster_graph(n,m,p)
		print("n=%d m=%d"%(n,m))
		densidade(n,grafo)
		print("\n")'''


n=50
while(n<=200):
	for m in range(1,3):
		#print("n=%d m=%d"%(n,m))
		grafo = nx.barabasi_albert_graph(n,m)
		#grafo=nx.powerlaw_cluster_graph(n,m,p)
		grafo_saida(grafo,n,m)
	print("\n")
	n=n+50

plt.grid(True)
plt.show()

#grafo=nx.powerlaw_cluster_graph(10,5,p)
#grafo_saida(grafo)
