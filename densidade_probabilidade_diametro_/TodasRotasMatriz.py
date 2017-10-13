#todas as rotas
def criar_matriz(tamanho):
	n=tamanho
	matrizAdjacente=[]
	for x in range(n):
		linha=[]
		for y in range(n):
			linha.append(0)
		matrizAdjacente.append(linha)
	matrizAdjacente[0][1]=3
	matrizAdjacente[1][0]=3

	matrizAdjacente[3][2]=4
	matrizAdjacente[2][3]=4

	matrizAdjacente[1][2]=2
	matrizAdjacente[2][1]=2

	matrizAdjacente[4][3]=3
	matrizAdjacente[4][3]=3

	matrizAdjacente[4][5]=2
	matrizAdjacente[5][4]=2

	matrizAdjacente[0][5]=2
	matrizAdjacente[5][0]=2

	return matrizAdjacente

def imprimir_matriz(Matriz):
	for x in range(len(Matriz)):
		print(Matriz[x])

def rotas(matriz,inicio,fim,listaSuprema,estrada=[],marcador=0):
	conexoes=[]
	caminhoDireto=[]
	estrada=estrada+[inicio]
	if inicio>=len(matriz) or fim>=len(matriz) :
		print("nó não presente")
		return None;
	for coluna in range(len(matriz)):
		if (matriz[inicio][coluna]!=0):
			conexoes.append(coluna)
			if (coluna==fim):
				caminhoDireto.append([inicio,coluna]) # se existir um caminho direto adicione
	#print("Conexoes com o ponto",inicio, ":",conexoes) #conexoes com o ponto inicial
	#se já encontrou o destino
	if fim in conexoes:
		estrada=estrada+[fim] #guarda rota feita até o momento
		marcador=20
		matriz[inicio][fim]=0 #desfazer rota já contabilizada
		possibilidades.append(estrada)
		return matriz
	listaSuprema.append(inicio)
	if marcador<10:
		for x in conexoes:
			if x not in listaSuprema:
				rotas(matriz,x,fim,listaSuprema,estrada)
	return None

def menor_caminho(matriz,possibilidades):
	caminhoCurto=list()
	for x in range(len(possibilidades)):
		somatorio=0
		for y in range(len(possibilidades[x])-1):
			vert1=possibilidades[x][y]
			vert2=possibilidades[x][y+1]
			somatorio=somatorio+matriz[vert1][vert2]
			#print("Somatório: ",somatorio)
		caminhoCurto.append(somatorio)
	menor=10000000
	posicao=-1
	for x in range(len(caminhoCurto)):
		if (caminhoCurto[x]<menor):
			menor=caminhoCurto[x]
			posicao=x

	if(posicao<len(possibilidades) and posicao!=-1):
		print("Menor caminho: ",possibilidades[posicao])
		return possibilidades[posicao]
	else:
		return None

'''possibilidades=[] #serve para guardar todos os caminhos encontrados
listaSuprema=[] #serve para marcar os nós pelos quais já passei

numero1=0
numero2=1
print("Ponto inicial:",numero1)
print("Ponto final:",numero2)

mat=criar_matriz(5)
imprimir_matriz(mat)

while(mat!=None):
	mat=rotas(mat,numero1,numero2,listaSuprema)
print(possibilidades)'''

matriz02=criar_matriz(6)
'''imprimir_matriz(matriz02)
menor_caminho(matriz02,possibilidades)'''


soma=0
tamanho=6
for x in range(len(matriz02)):
	for y in range(len(matriz02)):
		if(x!=y):
			possibilidades=[]
			listaSuprema=[]
			MATRIZ=criar_matriz(tamanho)
			while(MATRIZ!=None):
				MATRIZ=rotas(MATRIZ,x,y,listaSuprema)
			vetor=menor_caminho(matriz02,possibilidades)
			if vetor!=None:
				distancia=0
				for z in range(len(vetor)-1):
					linha=vetor[z]
					coluna=vetor[z+1]
					#print("Linha:",linha)
					#print("Coluna:",coluna)
					distancia=distancia+matriz02[linha][coluna]
					#print("Na marizz",matriz02[linha][coluna])
				print("Distancia:",distancia)
				soma=soma+distancia
media=soma/(tamanho*(tamanho-1))
print("Média das distâncias: %.2f"%media) #distancia media para grafo direcionado
