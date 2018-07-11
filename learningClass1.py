herois.py

class Heroi:

	def __init__(self, heroiVoa, possuiArma, lancaTeia, fraseHeroi):
		print("\nexecutando init ...")
		self.heroiVoa = heroiVoa
		self.possuiArma = possuiArma
		self.lancaTeia = lancaTeia
		self.fraseHeroi = fraseHeroi


	def frase(self):
		print(self.fraseHeroi)

	def detalhaHeroi(self):
		if self.heroiVoa:
			print("Herói voa")
		if self.lancaTeia:
			print("O herói lança teia")
		if self.possuiArma:
			print("O herói possui arma")
      
      
------------


from herois import Heroi


HomemAranha = Heroi(False, False, True,"")
print('\nHomem Aranha')
HomemAranha.detalhaHeroi()

ArqueiroVerde = Heroi(False, True, False,"")
print('\nArqueiro Verde')
ArqueiroVerde.detalhaHeroi()

heMan = Heroi(False, True, False,"Eu tenho a força")
print('\nHe-Man')
heMan.detalhaHeroi()
heMan.frase()
