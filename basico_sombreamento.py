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
# agora o objeto tem atributos com valores próprios

print(f'a:{valor.a} b:{valor.b} c:{valor.c}\n')
# o valor dos atributos da classes são os mesmos

del numeros.a
del numeros.b
del numeros.c
# excluindo atributos próprios do objeto

print(f'a:{numeros.a} b:{numeros.b} c:{numeros.c}')
# agora o objeto volta a herdar o valor dos atributos da classe
