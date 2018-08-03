nome_arquivo = input('Digite o nome do arquivo: ')
conteudo = input('Insira um texto no arquivo: ')


f = open(nome_arquivo,'+a')
f.write(conteudo)
f.close()

f = open(nome_arquivo)
content = f.read()
print(content)
f.close()
