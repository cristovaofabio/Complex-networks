import csv
with open('hero-network.csv') as csvfile:
	NovoArquivo = open('marvel.txt','w')
	reader = csv.DictReader(csvfile)
	for row in reader:
		ba="---"
		#print(row['hero1'],ba,row['hero2'])
		NovoArquivo.writelines(row['hero1']+ba+row['hero2']+"\n")


