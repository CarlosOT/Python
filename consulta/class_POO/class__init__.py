#Arquivo tipo_cao

class Canino:

	def __init__(self, grande, gordo, carinhoso, solta_pelo, raca, preco):

		self.raca = raca
		self.preco = preco

		self.grande = grande
		self.gordo = gordo
		self.carinhoso = carinhoso
		self.solta_pelo = solta_pelo

	def detalhamento(self):
		print('grande') if self.grande else print('pequeno')
		print('gordo') if self.gordo else print('porte normal')
		print('carinhoso') if self.carinhoso else print('um pouco agressivo')
		print('solta pelo') if self.solta_pelo else print('Não solta pelo')

	def nome_preco(self):
		print(f'Raça: {self.raca}')
		print(f'Preço: {self.preco}')
    
    
   #-------------------------------------------------------------------
   

from tipo_cao import Canino

labrador = Canino(True, False, True, True, 'Labrador','R$3000.00')

labrador.detalhamento()
labrador.nome_preco()
