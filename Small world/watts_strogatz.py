'''
Retorna um grafo small world de Watts-Strogatz.

Parâmetros:
	n (int) - O número de nós
	k (int) - Cada nó é unido com seus k vizinhos mais próximos em uma topologia anel.
	p (flutuante) - probabiliadade de adicionar outra aresta além do proposto pelo modelo small world

'''

import networkx as nx
import matplotlib.pyplot as plt

def draw_grafo(grafo):
	#grafo=nx.cubical_graph() #exemplo de grafo cúbico
	#nx.draw(grafo) # desenhar um grafo sem legenda
	nx.draw(grafo,node_color='green',with_labels=True)
	plt.show()


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
	print("Diâmetro: ",nx.diameter(grafo))
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


grafoB = gerarGrafo()
nos = len(grafoB) #quantidade de nós no grafo
arestas=grafoB.edges() #todas as arestas do grafo
quant_aresta=len(arestas) #quantidade de arestas no grafo

eficiencias=list()
dist_media=list()
diamet=list()
props=list()

#print("Para a base de dados: ")
#print("Diâmetro: ",nx.diameter(grafoB))

k=int((2*quant_aresta)/nos) #quantidade de vizinhos que cada nó deve ter

p=0.0
while(p<1):
	grafo=nx.watts_strogatz_graph(30,4,p)
	props.append(p)
	print(p)
	#grafo_saida(grafo,p)
	print("Diâmetro: ",nx.diameter(grafo))
	diamet.append(nx.diameter(grafo))
	distancia(grafo)
	print("")
	p=p+0.1

grafico(eficiencias,props,"Eficiência")
grafico(dist_media,props,"Distância média")
grafico(diamet,props,"Diâmetro")

plt.grid(True)
plt.show()

