from time import sleep

def somandoNumeros(): return lambda valor1, valor2 : valor1 + valor2

def subtracaoNumeros(): return lambda valor1, valor2 : valor1 - valor2

def multiplicaoNumeros(): return lambda valor1, valor2 : valor1 * valor2

def divisaoNumeros(): return lambda valor1, valor2 : valor1 / valor2


opcao = int(input('Escolha uma das opções operações: 1(+), 2(-), 3(*), 4(/), Sair(0) '))

if opcao == 0:
	print('Finalizando programa ... ')
	sleep(1)
	exit()

if opcao == 1:
	primeiroValor = int(input('Primeiro valor: '))
	segundoValor = int(input('Segundo valor: '))
	somando = somandoNumeros()
	resultado = somando(primeiroValor, segundoValor)
	print(f"A soma de {primeiroValor} e {segundoValor} é {resultado:.2f}")

elif opcao == 2:
	primeiroValor = int(input('Primeiro valor: '))
	segundoValor = int(input('Segundo valor: '))
	subtraindo = subtracaoNumeros()
	resultado = subtraindo(primeiroValor,segundoValor)
	print(f"A subtração de {primeiroValor} e {segundoValor} é {resultado:.2f}")

elif opcao == 3:
	primeiroValor = int(input('Primeiro valor: '))
	segundoValor = int(input('Segundo valor: '))
	multiplicando = multiplicaoNumeros()
	resultado = multiplicando(primeiroValor, segundoValor)
	print(f"A multiplicação de {primeiroValor} por {segundoValor} é {resultado:.2f}")

elif opcao == 4:
	primeiroValor = int(input('Primeiro valor: '))
	segundoValor = int(input('Segundo valor: '))
	dividindo = divisaoNumeros()
	resultado = dividindo(primeiroValor, segundoValor)
	print(f"A divisão de {primeiroValor} por {segundoValor} é {resultado:.2f}")




