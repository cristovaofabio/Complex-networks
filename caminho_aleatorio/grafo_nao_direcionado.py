import networkx as nx
from random import randint
import time

def gerarDict(dic=None,arestas=None,nos=None):
	if dic is None:
		dic=dict()
	if arestas is None:
		arestas=list()
	if nos is None:
		nos=list()
	marcador=0
	Abrir = open('base_de_dados/ipv6_TGF.txt','r')
	for linha in Abrir:
		vetor=linha.split() #quebrar linhas
		if(vetor[0]=="#"):
			marcador=1
		if (marcador!=1):
			numero1=int(vetor[0]) #primeiro numero
			if numero1 not in nos:
				nos.append(numero1)
			if numero1 not in dic:
				dic[numero1]=[]
		if (marcador==1 and vetor[0]!="#"):
			arestas.append(vetor)
			no1=int(vetor[0])
			no2=int(vetor[1])
			if no2 not in dic[no1]:
				if no2!=no1:
					dic[no1].append(no2)
			if no1 not in dic[no2]:
				if no2!=no1:
					dic[no2].append(no1)
	return dic


'''def gerarDict(grafo=None,arestas=None,nos=None):
	#nesta função estou gerando uma lista adjacente de saida
	if grafo is None:
		grafo=nx.Graph() #grafo não direcionado
	if arestas is None:
		arestas=list()
	if nos is None:
		nos=list()
	marcador=0
	Abrir = open('base_de_dados/ipv6_TGF.txt','r')
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
	#print(len(grafo))'''


#elaborado por Cristóvão
'''def percorrerRota(v1,v2,possibilidades=None):
	if possibilidades is None:
		possibilidades=[]
	possibilidades.append(v1) #usado para mostrar apenas uma rota 
	#possibilidades=possibilidades+[v1] #usado para mostrar todas as rotas
	if v1==v2:
		#print(possibilidades)
		EscreverArquivo(possibilidades)
		#return possibilidades
	for valor in dic[v1]:
		if valor not in possibilidades:
			if(valor!=v2 and dic[valor]!=[]):
				rota=percorrerRota(valor,v2,possibilidades)
				if (rota):
					casos.append(rota)
			elif(valor==v2):
				rota=percorrerRota(valor,v2,possibilidades)
				if (rota):
					casos.append(rota)
				#print(rota)
	return None'''


#Proposto em sala de aula
def caminho_aleatorio(Lista, origem,destino):
	i=0
	numero=origem
	caminho=list()
	caminho.append(origem)
	c=list()
	while numero!=destino:
		c.append(numero)
		ultimo_elemento=c[-1] #utimo elemento da lista
		tam_lista_elemento=len(Lista[ultimo_elemento])
		w=Lista[ultimo_elemento][randint(0,(tam_lista_elemento-1))]
		if w not in c:
			c.append(w)		
			i<-i+1
			#print(w)
			caminho.append(w)
		numero=w
	return caminho

'''def EscreverArquivo(vetor):
	Arquivo = open('rotas.txt','a') # O 'a' serve para atualizar o arquivo, ou seja, sem perder antigas informações
	Arquivo.writelines(str(vetor)+"\n") #escrever cada número em uma linha
	Arquivo.close()'''

def distancia_media(rotas):
	contador=0
	somatorio=0
	for x in rotas:
		contador=contador+1
		somatorio=somatorio+(len(x)-1)
		#print(x,(len(x)-1))
	print("Média das distâncias: ",somatorio/contador)
	#print(matriz)

Rotas=list()
dic = gerarDict()
caminho_aleatorio(dic,5,6)
pares=list()
rotas=list()
for x in dic:
	inicio = time.time() #tempo inicial
	for y in dic:
		if ([x,y] not in pares and x!=y):
			pares.append([x,y])
			pares.append([y,x])
			print([x,y])
			#casos=[]
			rotas.append(caminho_aleatorio(dic,x,y))
	fim = time.time()
	tempo_estimado=len(dic)*len(dic)*(fim - inicio)
	print("Nó %d. Tempo busca de todas as rotas: %f"%(x,(tempo_estimado/60)))

#print(rotas)
#print(percorrerRota(0,0))
#print(Rotas)

distancia_media(rotas)

'''grafo = gerarDict()
#lista=list(nx.all_shortest_paths(grafo,source=0,target=3)) #todos os caminhos mais curtos
lista=list(nx.shortest_path(grafo,source=0,target=3)) #apenas um caminho curto
print(lista)'''
