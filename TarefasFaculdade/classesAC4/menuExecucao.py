print('''

Faculdade Impacta - Sistema de Cadastros

1 - Aluno

2 - Professor

00 - Sair
''')

while True:
    opcao = input('\nopção: ')
    if opcao == '1':
        from registrosAluno import *
    elif opcao == '2':
        from registrosProfessor import *
    elif opcao == "00":
        exit()
    else:
        print('opção inválida')
        continue