while True:
	entrada = input('Entrada: ')
	if entrada == '':
		continue
	if entrada == '0':
		break
	entrada = entrada.replace(' ','')
	for i in entrada:
		print(i, end='')
	print('')
	continue
