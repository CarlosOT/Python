#arquivo gostosPessoais.py

class gostoParticular:
	def __init__(self, calor, frio, estudar, viajar, fraseFavorita):
		
		print('\nexecutando o init ...')
		self.calor = calor
		self.frio = frio
		self.estudar = estudar
		self.viajar = viajar
		self.fraseFavorita = fraseFavorita

	def frase(self):
		print(self.fraseFavorita)

	def gostosPessoais(self):
		if self.calor:
			print('gosta do calor')
		else:
			print('não gosta calor')

		if self.frio:
			print('gosta do frio')
		else:
			print('não gosta do frio')

		if self.estudar:
			print('gosta de estudar')
		else:
			print('Não gosta de estudar')

		if self.viajar:
			print('gosta de viajar')
		else:
			print('não gosta de viajar')


------------


from gostosPessoais import gostoParticular


joao = gostoParticular(False, True, False, True,"wathever you do, do well")
print('\nGosto pessoal do João: ')
joao.gostosPessoais()
joao.frase()


mariana = gostoParticular(True, False, False, True,"what you won't do, do for love")
print('\nGosto pessoal da Mariana: ')
mariana.gostosPessoais()
mariana.frase()
