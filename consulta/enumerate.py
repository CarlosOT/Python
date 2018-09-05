lista_frutas = []

while True:
	frutas = input('Adicione frutas na lista ou "s" para sair: ')
	if frutas == 's':
		break
	else:
		lista_frutas.append(frutas)


for indice, fruta in enumerate(lista_frutas):
	print(f"{indice + 1} - {fruta}")
