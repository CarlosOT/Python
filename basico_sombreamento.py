class valor():
	a = 1
	b = 2
	c = 3

numeros = valor()
print(f'a:{numeros.a} b:{numeros.b} c:{numeros.c}\n')
# o objeto herda o valor dos atributos da classe  (herança)


numeros.a = 3
numeros.b = 2
numeros.c = 1
print(f'a:{numeros.a} b:{numeros.b} c:{numeros.c}\n')
# agora o valor desses atributos são do próprio objeto

del numeros.a
del numeros.b
del numeros.c
# excluindo atributos próprios do objeto

print(f'a:{numeros.a} b:{numeros.b} c:{numeros.c}')
# agora o objeto volta a herdar o valor dos atributos da classe
