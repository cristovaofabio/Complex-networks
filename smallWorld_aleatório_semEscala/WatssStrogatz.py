'''
Retorna um grafo small world de Watts-Strogatz.

Parâmetros:
	n (int) - O número de nós
	k (int) - Cada nó é unido com seus k vizinhos mais próximos em uma topologia anel.
	p (flutuante) - probabiliadade de mover uma aresta do lugar

'''

import networkx as nx
import matplotlib.pyplot as plt

def draw_grafo(grafo):
	#grafo=nx.cubical_graph() #exemplo de grafo cúbico
	#nx.draw(grafo) # desenhar um grafo sem legenda
	nx.draw(grafo,node_color='green',with_labels=True)
	plt.show()

def percorrer_dicionario(dicionario,p):
	eixoX=list()
	eixoY=list()

	for x in dicionario:
		eixoX.append(x)
		eixoY.append(dicionario[x])
		print(x,dicionario[x])

	legenda="Para p = %.2f"%p
	plt.plot(eixoX, eixoY,label=legenda)
	plt.xlabel("Graus")
	plt.ylabel("Quantidade")
	plt.legend()


def grafico(valores,prs,legenda):

	plt.plot(prs, valores,label=legenda)
	plt.xlabel("p")
	plt.ylabel("valores")
	plt.legend()


def grafo_saida(grafo,p):
	soma=0
	graus=dict()
	for x in grafo:
		arest=len(grafo[x])

		if (arest not in graus):
			graus[arest]=1
		else:
			graus[arest]=graus[arest]+1

		#print("Grau de saida do nó %d: %d"%(x,arest))
		soma=soma+arest
	percorrer_dicionario(graus,p) #dicionario com a frequência de cada grau

	#print("Quantidade de arestas:",soma/2)
	#print("Quantidade media de vizinhos: %.1f"%(soma/len(grafo)))


def CaminhoExiste(G,no1,no2):
	try:
		sp = nx.shortest_path(G,no1,no2)
	except nx.NetworkXNoPath:
		return False
	return True

def distancia(grafo):
	total=0
	contador=0
	SomaEfi=0
	for x in grafo:
		for y in grafo:
			if y!=x:
				if(CaminhoExiste(grafo,x,y)):
					#encontrar o caminho caminho mais curto entre um par de nós
					vetor=nx.dijkstra_path(grafo,x,y)
					soma=0.0
					for num in range(len(vetor)-1):
						numero1=vetor[num]
						numero2=vetor[num+1]
						#distancia do percurso
						soma=soma+1
				else:
					soma=1000000000000000000
				contador=contador+1
				#soma das eficiencias(cada par de nós possue apenas uma)
				SomaEfi=SomaEfi+(1/soma)
				#soma das distância
				total=total+soma
	dist=(total/contador)
	print("Distancia média: %.2f"%dist)
	dist_media.append(dist)
	print("Eficiencia média: %.2f"%(SomaEfi/contador))
	eficiencias.append((SomaEfi/contador))

eficiencias=list()
dist_media=list()
diamet=list()
props=list()

#print("Para a base de dados: ")
#print("Diâmetro: ",nx.diameter(grafoB))

p=0.0
'''while(p<1):
	grafo=nx.watts_strogatz_graph(30,4,p)
	props.append(p)
	print(p)
	#grafo_saida(grafo,p)
	diametro=nx.diameter(grafo)
	print("Diâmetro: ",diametro)
	diamet.append(diametro)
	distancia(grafo)
	print("")
	p=p+0.1

#Para gerar os gráficos
grafico(eficiencias,props,"Eficiência")
grafico(dist_media,props,"Distância média")
grafico(diamet,props,"Diâmetro")

plt.grid(True)
plt.show()'''
grafo=nx.watts_strogatz_graph(30,4,1)
draw_grafo(grafo)

