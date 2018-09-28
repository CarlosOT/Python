def removeSpace(string):
    string = string.replace(' ','')
    return string

file = open('etiquetas.txt')
file2 = open('Códigos&Pedidos.txt','+a')
content = file.read()

while True:
    try:
        indice1 = content.index('Nº Loja Virtual: ')
    except ValueError:
        break
    
    indice2 = indice1 + 22
    contentSlice = f'{content[indice1:indice2]}'
    content = content.replace(contentSlice,' ')
    file2.write(contentSlice)
    indice2 = content.index('BR')
    indice1 = indice2 - 17
    contentSlice = f'{content[indice1:indice2 + 2]}'
    content = content.replace(contentSlice,' ')
    contentSlice = removeSpace(contentSlice)
    file2.write(contentSlice)
    file2.write('\n+-------------------+\n')

file2.close()

