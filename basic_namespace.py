def funcao_externa():
	a = 80
	b = 20

	print(
		f'Imprimindo "a" em funcao_externa: {a}\n'	
		f'Imprimindo "b" em funcao_externa: {b}\n'
		)

	def funcao_interna():
		a = 70
		b = 25
		c = 30

		print(
			f'Imprimindo "a" em funcao_interna: {a}\n'
			f'Imprimindo "b" em funcao_interna: {b}\n'
			f'Imprimindo "c" em funcao_interna: {c}\n'
			)

	print(f'Imprimindo "b" mais uma vez em funcao_externa: {b}\n')	
	funcao_interna()
	print(f'Imprimindo "b" de novo em funcao_externa: {b}')


a = 10
print(f'\nImprimindo "a" no escopo global: {a}\n')

funcao_externa()


print(f'\nImprimindo "a" de novo no escopo global: {a}')
