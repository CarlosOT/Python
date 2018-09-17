import os
import shutil

def readFile(PrincipalFolder, directory, ContentSearch, destination):
	os.chdir('/home/carlos/Desktop/'+ PrincipalFolder)
	ListFile = os.listdir(directory)
	os.chdir('./' + directory) 
	for file in ListFile:
		f = open(file)
		content = f.read()
		if ContentSearch in content:
			shutil.copy(file, destination)
			f.close()
			print(f'\n!!! Achei no diretório {directory}!!!\n')
				
			

				

currentPath = input('Caminho onde se encontra a pasta principal (ex. "/home/exemplo/Desktop"): ')
if currentPath == '00':
	exit()
else:
	os.chdir(currentPath) 

PrincipalFolder = input('Nome da pasta principal: ')
if PrincipalFolder == '00':
	exit()
else:
	directories = os.listdir(PrincipalFolder)

destination = input('Destino onde a cópia do arquivo será movida: ')
if destination == '00':
	exit()	

while True:
	ContentSearch = input('Conteúdo a ser procurado: ')
	if ContentSearch == '00':
		exit()
	else:
		for directory in directories:
			readFile(PrincipalFolder, directory, ContentSearch, destination)





