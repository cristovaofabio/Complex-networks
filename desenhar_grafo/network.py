import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

grafo= nx.Graph() #criar um grafo nao direcionado
#grafo= nx.DiGraph() #criar um grafo direcionado

grafo.add_node(1)
grafo.add_node(2)
grafo.add_node(3)
grafo.add_node(4)

#caso não especifique o"weight", o peso da aresta por padrão é igual a 1
grafo.add_edge(1, 2,weight=1)
grafo.add_edge(2, 3, weight=1)
grafo.add_edge(1, 3, weight=1)
grafo.add_edge(3, 4, weight=1)

def gerarGrafo(grafo=None,arestas=None,nos=None):
	#Nesta função estou gerando uma lista adjacente de saida
	if grafo is None:
		#criar um grafo nao direcionado
		grafo= nx.Graph()
		#criar um grafo direcionado
		#grafo= nx.DiGraph()
	if arestas is None:
		arestas=list()
	marcador=0
	Abrir = open('facebookTGF.txt','r')
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
	return grafo

def distancia(grafo):
	total=0
	contador=0
	SomaEfi=0
	for x in grafo:
		for y in grafo:
			if y!=x:
				vetor=nx.dijkstra_path(grafo,x,y) #encontrar o caminho caminho mais curto entre um par de nós
				soma=0.0
				for num in range(len(vetor)-1):
					numero1=vetor[num]
					numero2=vetor[num+1]
					soma=soma+grafo[numero1][numero2]['weight'] #distancia do percurso
				contador=contador+1
				SomaEfi=SomaEfi+(1/soma) #soma das eficiencias(cada par de nós possue apenas uma)
				total=total+soma #soma das distância
	dist=(total/contador)
	print("Distancia média: %.2f"%dist)
	print("Eficiencia média: %.2f"%(SomaEfi/contador))
	

def draw_grafo(grafo):
	#grafo=nx.cubical_graph() #exemplo de grafo cúbico
	#nx.draw(grafo) # desenhar um grafo sem legenda
	nx.draw(grafo,node_color='green',with_labels=True)
	plt.show()

def draw_grafo_aresta(grafo):
	pos=nx.spring_layout(grafo)
	nx.draw(grafo,pos,with_labels=True)
	# specifiy edge labels explicitly
	edge_labels=dict([((u,v,),d['weight'])
	for u,v,d in grafo.edges(data=True)])
	nx.draw_networkx_edge_labels(grafo,pos,edge_labels=edge_labels)
	# show graphs
	plt.show()

def histograma_grau(G):
	nos=list()
	for x in G:
		nos.append(x)
	#grau de saída de cada nó, apenas para grafos direcionados
	#grau_saida=G.out_degree(nos)
	#grau de entrada de cada nó, apenas para grafos direcionados
	#grau_entrada=G.in_degree(nos)
	# Calculando o grau para cada nó(grau de entrada ou saida)
	deg = nx.degree(G)
	# Transforma num DataFrame (pandas)
	degree = pd.DataFrame.from_dict(data=deg, orient='index')
	# Apresenta apenas os valores do dicionário com os graus
	#deg.values()
	plt.hist(degree, color="green", alpha=.5)
	plt.title('Histograma do Grau')
	plt.xlabel("Grau")
	plt.ylabel("Quantidade de nós")
	plt.show()

#grafo=gerarGrafo()
distancia(grafo)
'''
#valor=nx.diameter(grafo)
#print("Diâmetro:",valor) #maior distancia entre as menores distâncias entre vértices
#print("Densidade: %.2f"%nx.density(grafo))'''
#histograma_grau(grafo)
#draw_grafo_aresta(grafo)
#draw_grafo(grafo)
