# arquivo leitura.py

def lerArquivo(nomeArquivo):
    f = open(nomeArquivo)
    content = f.read()
    print(content)
    f.close()


import leitura

nome = input('Nome do arquivo: ')
conteudo = input(f'Conteúdo a ser armazenado em {nome}: ')

f = open(nome,'+a')
f.write(conteudo)
f.close()

leitura.lerArquivo(nome)
