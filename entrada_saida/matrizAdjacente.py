import time

def criarMatriz(tamanho):
	matriz=[]
	for x in range(tamanho):
		lista=list()
		for y in range(tamanho):
			lista.append(0)
		matriz.append(lista)
	return matriz

def preencherMatriz(matriz,arestas):
	for pares in arestas:
		linha=int(pares[0])
		coluna=int(pares[1])
		matriz[linha][coluna]=1
	return matriz

def imprimirMatriz(matriz):
	tamanho=len(matriz)
	for x in range(tamanho):
		print(matriz[x])

def MatrizAdjacente(nos=None,arestas=None):
	Abrir = open('grafoTGF.txt','r')
	marcador=0
	if nos is None:
		nos=list()
	if arestas is None:
		arestas=list()
	for linha in Abrir:
		vetor=linha.split() #quebrar linhas

		if(vetor[0]=="#"):
			marcador=1
		if (marcador!=1):
			if vetor[0] not in nos:
				nos.append(vetor[0])
		if (marcador==1 and vetor[0]!="#"):
			arestas.append(vetor)
	valores=[]
	for num in range(len(nos)):
		valores.append(int(nos[num]))
	tamanho=max(valores)+1
	quant_nos=int(len(nos))
	print("Nos:",quant_nos)
	quant_arest=int(len(arestas))
	#print(arestas)
	max_arest=quant_nos*(quant_nos-1)#calculo para grafos direcionados
	Matriz=criarMatriz(tamanho)
	Matriz=preencherMatriz(Matriz,arestas)
	print("Arestas",len(arestas))
	print("Densidade: %.2f"%(quant_arest/max_arest))
	return Matriz

def procurar_aresta(grafo):
	arquivo = open('nos','r')
	for linha in arquivo:
		vetor=linha.split()
		num1=int(vetor[0])
		num2=int(vetor[1])
		inicio=time.time()
		grafo[num1][num2]
		fim=time.time()
		print("Tempo:",(fim-inicio))

Matriz=[]
Matriz=MatrizAdjacente()
procurar_aresta(Matriz)
#imprimirMatriz(Matriz)
