while True:
	entrada = input('Entrada: ')
	if len(entrada) == 0:
		continue
	if entrada == '0':
		break
	entrada = entrada.replace(' ','')
	for i in entrada:
		print(i, end='')
	print('')
	continue