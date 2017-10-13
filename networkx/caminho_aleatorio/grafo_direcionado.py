import networkx as nx

def gerarDict(grafo=None,arestas=None,nos=None):
	#nesta função estou gerando uma lista adjacente de saida
	if grafo is None:
		grafo=nx.DiGraph() #grafo direcionado
	if arestas is None:
		arestas=list()
	if nos is None:
		nos=list()
	marcador=0
	Abrir = open('teste','r')
	for linha in Abrir:
		vetor=linha.split() #quebrar linhas
		if(vetor[0]=="#"):
			marcador=1
		if (marcador!=1):
			numero=int(vetor[0])
			if numero not in nos:
				nos.append(numero)
		if (marcador==1 and vetor[0]!="#"):
			arestas.append(vetor)
			no1=int(vetor[0])
			no2=int(vetor[1])
			grafo.add_edge(no1,no2,weight=1)
	return grafo
	#print(len(grafo))

def has_path(G, source, target):
	try:
		sp = nx.shortest_path(G,source, target)
	except nx.exception.NetworkXNoPath:
		return False
	return True

grafo = gerarDict()
#lista=list(nx.all_shortest_paths(grafo,source=0,target=3)) #todos os caminhos mais curtos
no1=1
no2=0
listaCaminhos=list()
if(has_path(grafo,no1,no2)==True):
	lista=list(nx.all_shortest_paths(grafo,source=0,target=3)) #apenas um caminho curto
	print(lista)
else:
	print("Não existe uma rota")
