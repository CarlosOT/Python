# meu código

from time import sleep

def somandoNumeros(): return lambda valor1, valor2 : valor1 + valor2

def subtracaoNumeros(): return lambda valor1, valor2 : valor1 - valor2

def multiplicaoNumeros(): return lambda valor1, valor2 : valor1 * valor2

def divisaoNumeros(): return lambda valor1, valor2 : valor1 / valor2


opcao = int(input('Escolha uma das operações: 1(+), 2(-), 3(*), 4(/), Sair(0) '))

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
	
	
---------


# código do professor

soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y

operacao = int(input(" 1: Soma\n 2: Subtração\n 3: Multiplicação\n 4: Divisão\n Informe o número da operação: "))
if operacao not in [1, 2, 3, 4]:
    print("Operação inválida.")
    exit()

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

if operacao == 1:
    print("Resultado da soma: ", soma(numero1, numero2))
elif operacao == 2:
    print("Resultado da subtração: ", subtracao(numero1, numero2))
elif operacao == 3:
    print("Resultado da multiplicação: ", multiplicacao(numero1, numero2))
else:
    print("Resultado da divisão: ", divisao(numero1, numero2))





