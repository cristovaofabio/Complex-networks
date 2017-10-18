#dic = {'A':['B','C'],'B':['A','C','D'],'C':['A','B','D'],'D':['B','C']}
#Abaixo se encontra uma topologia em estrela
dic = { "A" : { "B" : 1},
          "B" : { "D":2, "C":4,"A":1 },
          "C" : { "B":4 },
          "D" : { "B": 2 },
          }

def gerarDict(dic=None,arestas=None,nos=None):
	#Nesta função estou gerando uma lista adjacente de saida
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
			tamanho=max(nos)+1
		if (marcador!=1):
			numero=int(vetor[0])
			if numero not in nos:
				nos.append(numero)
			if numero not in dic:
				dic[numero]={}
		if (marcador==1 and vetor[0]!="#"):
			arestas.append(vetor)
			peso=1
			if len(vetor)==3:
				peso = int(vetor[2]) #caso tenha aresta com peso
			no1=int(vetor[0])
			no2=int(vetor[1]) 
			if no2 not in dic[no1]:
				dic[no1][no2]=peso
			#A Linha abaixo é utilizada para grafos não direcionados
			if no1 not in dic[no2]:
				dic[no2][no1]=peso
	return dic
	#print(dic)

def caminho(v1,v2):
	for chave in  dic:
		encontrar=0
		if(chave==v1):
			for x in dic[chave]:
				if(x==v2):
					print("Caminho existente")
					encontrar=1
			if (encontrar==0):
				print("Caminho não existente")

#caminho('A','D')

def percorrerRota(v1,v2,possibilidades=None):
	if possibilidades is None:
		possibilidades=[]
	#possibilidades.append(v1) #usado para mostrar apenas uma rota 
	possibilidades=possibilidades+[v1] #usado para mostrar todas as rotas
	if v1==v2:
		return possibilidades
	for valor in dic[v1]:
		if valor not in possibilidades:
			rota=percorrerRota(valor,v2,possibilidades)
			if (rota):
				casos.append(rota)
				#print(rota)
	return None

def menor_distancia(casos,dic):
	caminho=dict()
	menor=1000000
	for i in range(len(casos)):
		soma=0
		for j in range(len(casos[i])-1):
			pri = int(casos[i][j])
			seg = int(casos[i][j+1])
			soma=soma+dic[pri][seg]
		if(menor>soma):
			caminho=dict()
			menor=soma
			caminho[menor]=casos[i] #coluna
	distancia=0
	for chave in caminho:
		distancia=chave
		#print("Menor rota: ",caminho[chave])
		#print("Distância: ",distancia)
		#print("---------------------------")
	return distancia

def maior_distancia(casos,dic):
	caminho=dict()
	menor=-1000000
	maior=0
	for i in range(len(casos)):
		soma=0
		for j in range(len(casos[i])-1):
			pri = int(casos[i][j])
			seg = int(casos[i][j+1])
			soma=soma+dic[pri][seg]
		if(menor<soma):
			caminho=dict()
			menor=soma
			caminho[menor]=casos[i] #coluna
	distancia=0
	for chave in caminho:
		distancia=chave
		print("Maior rota: ",caminho[chave])
		print("Distância: ",distancia)
		print("---------------------------")
		t=len(caminho[chave])-1
		if maior<t:
			maior=t
	#return distancia
	return maior

def distancias(casos,dic):
	somaCaminhos=0
	for i in range(len(casos)):
		soma=0
		for j in range(len(casos[i])-1):
			pri = casos[i][j]
			seg = casos[i][j+1]
			soma=soma+dic[pri][seg]
		somaCaminhos=somaCaminhos+soma
	print("soma: ",soma)
	return somaCaminhos

def densidade(dic):
	aresta=0
	for chave in dic:
		aresta=aresta+len(dic[chave])
	aresta=aresta/2 #se não for direcionado
	quantNos=len(dic)
	#quantMaxima=quantNos*(quantNos-1) #se for direcionado
	quantMaxima=quantNos*(quantNos-1)/2 #se não for direcionado
	print("Densidade: %.2f"%(aresta/quantMaxima))

def probabilidade(dic,grau):
	contador=0
	for chave in dic:
		if len(dic[chave])==grau:
			contador=contador+1
	prob=contador/len(dic)
	print("Probabilidade de econtrar um nó com grau %d: %.2f"%(grau,prob))

	'''graus=dict()
	for chave in dic:
		gr=len(dic[chave])
		if gr not in graus:
			graus[gr]=1
		else:
			quant=graus[gr]+1
			graus[gr]=quant

	for chave in graus:
		prob=graus[chave]/len(dic)
		print("Probabilidade de econtrar um nó com grau %d: %.2f"%(chave,prob))'''

soma=0
diamet=0
contador=0
dic=gerarDict()

'''for chave1 in dic:
	for chave2 in dic:
		if(chave1!=chave2):
			casos=[]
			percorrerRota(chave1,chave2)
			result=menor_distancia(casos,dic)#apenas as menores distâncias
			resultM=maior_distancia(casos,dic)#apenas as maiores distâncias
			if diamet<resultM:
				diamet=resultM
			if result!=0:
				contador=contador+1
				soma=soma+result'''


'''tamanho=(len(dic))
tamanho=tamanho*(tamanho-1)/2 #direcionado ou não direcionado
#A distancia media é a soma de todas as distancias
print("Distância média: %.2f"%(soma/contador))
print("Diâmetro:",diamet)'''
densidade(dic)
probabilidade(dic,2)
'''casos=[]
percorrerRota("A","F")
print("Todas as rotas: ",casos)
maior_distancia(casos,dic)'''
