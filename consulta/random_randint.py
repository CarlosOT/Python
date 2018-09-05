from random import *

def sorteio(parametro):
	if parametro == 1:
		print('\nNão foi dessa vez, tente de novo!')
	elif parametro == 2:
		print('\nhummm, quase!')
	elif parametro == 3:
		print('\nParabéns, você ganhou!')
	elif parametro == 4:
		print('\nuffa, quase você acertou!')
	elif parametro == 5:
		print('\nPassou longe!')

numeroAleatorio = randint(1,5)
sorteio(numeroAleatorio)

print(f'Número sorteado: {numeroAleatorio}\n')
