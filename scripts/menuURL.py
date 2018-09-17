import webbrowser


while True:
    print('''
    Abrir no navegador

    1 - How to automate boring stuff with python
    2 - Github
    3 - Trello
    4 - Classroom
    5 - Facebook
    6 - Banco Inter
    7 - Phpmyadmin
    
''')
    opcao = input('\nOpção:')
    if opcao.isdecimal() == False:
        print('\n!!! Inválido !!!\n')
        continue
    if opcao == '':
        print('\n!!! Inválido !!!\n')
        continue
    elif opcao == '00':
        exit()
    elif opcao == '1':
        automate = webbrowser.open('https://automatetheboringstuff.com/')
        continue
    elif opcao == '2':
        github = webbrowser.open('https://github.com/CarlosOT')
        continue
    elif opcao == '3':
        trello = webbrowser.open('https://trello.com/b/UOwJwicu/pessoal')
    elif opcao == '4':
        classroom = webbrowser.open('https://classroom.google.com/u/1/h')
    elif opcao == '5':
        facebook = webbrowser.open('https://www.facebook.com/')
    elif opcao == '6':
        inter = webbrowser.open('https://internetbanking.bancointer.com.br/cartao/consultarCartoes.jsf')
    elif opcao == '7':
        phpmyadmin = webbrowser.open('http://localhost/phpmyadmin/')
    else:
        print('\n!!! Inválido !!!\n')
        continue
