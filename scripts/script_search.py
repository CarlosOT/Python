import os
import shutil

def readFile(directory, ContentSearch):
	os.chdir('path') # ex. '/home/exemplo/Desktop/pastaPrincipal'
	ListFile = os.listdir(directory)
	os.chdir('./' + directory) # ex. '/home/exemplo/Desktop/pastaPrincipal/arquivo '
	for file in ListFile:
		f = open(file)
		content = f.read()
		if ContentSearch in content:
			shutil.copy(file, 'path' ) # ex. '/home/exemplo/Desktop/pastaPrincipal'
			f.close()
			exit()

os.chdir('path') # ex. '/home/exemplo/Desktop'
folder = input('Nome da pasta principal que contém as pastas com os arquivos: ')
directories = os.listdir(folder)
ContentSearch = input('Conteúdo a ser procurado: ')

for directory in directories:
	readFile(directory, ContentSearch)





