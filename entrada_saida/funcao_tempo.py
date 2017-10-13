import time #utilizado para calcular o tempo de execucao de um programa(o tempo é calculado em segundos)

def funcao():
	NovoArquivo = open('TesteTempos.txt','w')
	for x in range(1,6):
		valor=x*10000
		inicio=time.time() #tempo inicial
		for y in range(valor):
			a=3
		fim=time.time() #tempo final
		tempo=fim-inicio
		NovoArquivo.writelines(str(tempo)+"\n")
		#print(fim-inicio)

funcao()
