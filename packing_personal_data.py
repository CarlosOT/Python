def user(nome, sobrenome, idade):
	print(f"\nOlá meu nome é {nome} {sobrenome} tenho {idade} de idade, prazer!")


nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = input('Digite sua idade: ')

dadoPessoais = (nome, sobrenome, idade)

user(*dadoPessoais)


permissao = input('\nDigite "t" para troca de dados ou qualquer tecla para sair: ')
permissaoUpper = permissao.upper()

if permissaoUpper != 'T':
	exit()
else:
	nome = input('Digite seu nome: ')
	sobrenome = input('Digite seu sobrenome: ')
	idade = input('Digite sua idade: ')

	dados_troca = {'idade' : idade, 'sobrenome' : sobrenome, 'nome' : nome}

	user(dados_troca.get('nome'), dados_troca.get('sobrenome'), dados_troca.get('idade'))

	

# trocaDados = {'nome' : nome, 'sobrenome' : sobrenome, 'idade' : idade}
# user(*trocaDados.values())
