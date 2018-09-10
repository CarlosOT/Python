from allClasses import *

print('\n*Os dados do aluno serão salvos em um arquivo\n')

while True:
    while True: # validando nome
        try:
            nome = input('\nNome: ').capitalize()
            if nome == '':
                print('\n!!! esse campo não pode ser nulo !!!\n')
                continue
            validaString = int(nome)
            print('\n!!! Valor Inválido !!!\n')
            continue
        except:
            break
    while True: # validando endereço
        endereco = input('Endereço: ').capitalize()
        if len(endereco) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        else:
            break
    while True: # validando data de nascimento
        dataNascimento = input('Data de nascimento (ex.10-06-1996): ')
        if dataNascimento == '':
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if len(dataNascimento) != 10:
            print('\n!!! Valor Inválido !!!\n')
            continue
        contaHifen = dataNascimento.count('-')
        if contaHifen != 2:
            print('\n!!! Valor Inválido !!!\n')
            continue
        validaDataNascimento = dataNascimento.split('-')
        if len(validaDataNascimento) != 3:
            print('\n!!! Valor Inválido !!!\n')
            continue
        listaTamanho = []
        for i in validaDataNascimento:
            tamanhoElemento = len(i)
            listaTamanho.append(tamanhoElemento)
        if listaTamanho != [2,2,4]:
            print('\n!!! Valor Inválido !!!\n')
            continue
        contaErros = 0
        for i in validaDataNascimento:
            try:
                validaNumero = int(i)
            except:
                contaErros += 1
        if contaErros != 0:
            print('\n!!! Valor Inválido !!!\n')
            continue
        else:
            break
    while True:  # validando sexo
        sexo = input('Sexo [M] ou [F]: ').upper()
        if sexo == 'X':
            exit()
        if len(sexo) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('\n!!! Valor Inválido !!!\n')
            continue
    while True: # validando telefone celular
        telefoneCelular = input('Telefone Celular (ex.11 97865-8909): ')
        if telefoneCelular == '':
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if len(telefoneCelular) > 13:
            print('\n!!! Valor Inválido !!!\n')
            continue
        contaHifen = telefoneCelular.count('-')
        if contaHifen != 1:
            print('\n!!! Valor Inválido !!!\n')
            continue
        validaCel = telefoneCelular.split('-')
        try:
            if validaCel[0][2] == ' ':
                validaCel2 = validaCel[0].replace(validaCel[0][2],'')
            else:
                print('\n!!! Valor Inválido !!!\n')
                continue
        except:
            print('\n!!! Valor Inválido !!!\n')
            continue
        if len(validaCel2) > 7 or len(validaCel[1]) != 4:
            print('\n!!! Valor Inválido !!!\n')
            continue
        if (validaCel2.isdecimal() == True) and (validaCel[1].isdecimal() == True):
            break
        else:
            print('\n!!! Valor Inválido !!!\n')
            continue
    while True: # validando telefone residencial
        telefoneResidencial = input('Telefone Residencial (ex.11 3456-8909): ')
        if telefoneResidencial == '':
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if len(telefoneResidencial) > 12:
            print('\n!!! Valor Inválido !!!\n')
            continue
        contaHifen = telefoneResidencial.count('-')
        if contaHifen != 1:
            print('\n!!! Valor Inválido !!!\n')
            continue
        validaResidencial = telefoneResidencial.split('-')
        try:
            if validaResidencial[0][2] == ' ':
                validaResidencial2 = validaResidencial[0].replace(validaResidencial[0][2],'')
            else:
                print('\n!!! Valor Inválido !!!\n')
                continue
        except:
            print('\n!!! Valor Inválido !!!\n')
            continue
        if len(validaResidencial2) > 7 or len(validaResidencial[1]) != 4:
            print('\n!!! Valor Inválido !!!\n')
            continue
        if (validaResidencial2.isdecimal() == True) and (validaResidencial[1].isdecimal() == True):
            break
        else:
            print('\n!!! Valor Inválido !!!\n')
            continue
    while True: # validando o e-mail
        email = input('Email: ').lower().replace(' ','')
        if len(email) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if '@' not in email or '.' not in email:
            print('\n!!! Email Inválido, faltou "." ou "@" !!!\n')
            continue
        contaArroba = email.count('@')
        if contaArroba != 1:
            print('\n!!! Email Inválido, tem mais de um "@" !!!\n')
            continue
        validaEmail = email.split('.')
        tamanhoEmail = len(validaEmail)
        if validaEmail[tamanhoEmail - 1] != 'com':
            print('\n!!! Email Inválido, não tem ".com" no final !!!\n')
            continue
        detectaArroba = len(validaEmail[tamanhoEmail - 2])
        if validaEmail[tamanhoEmail - 2][detectaArroba - 1] == '@':
            print('\n!!! Email Inválido, não tem servidor depois do "@" !!!\n')
            continue
        if validaEmail[tamanhoEmail - 2][0] == '@':
            print('\n!!! Email Inválido, tem um "." antes do "@" !!!\n')
            continue
        else:
            break
    while True: # validando o estado civil
        listaCivil = ['SOLTEIRO','CASADO','DIVORCIADO','VIÚVO']
        estadoCivil = input('Estado Civil: ').upper().replace(' ','')
        if estadoCivil == 'VIUVO':
            estadoCivil = estadoCivil.replace('VIUVO','VIÚVO')
        if len(estadoCivil) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if estadoCivil not in listaCivil:
            print('\n!!! Inválido !!!\n')
            print('\n*opções disponíveis: Solteiro, Casado, Divorciado e Viúvo\n')
            continue
        else:
            estadoCivil = estadoCivil.capitalize()
            print(estadoCivil)
            break
    while True: # validando RA
        ra = input('Ra: ')
        if len(ra) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if ra.isdecimal() == True and len(ra) == 7:
            break
        else:
            print('\n!!! Valor Inválido, o RA precisa ser um sequência de 7 números!!!\n')
            continue
    while True: # validando nome do arquivo
            nomeArquivo = input('\nDefina o nome do arquivo onde os dados serão salvos: ')
            if len(nomeArquivo) == 0:
                print('\n!!! esse campo não pode ser nulo !!!\n')
                continue
            elif ('.txt' in nomeArquivo):
                print('\n#!#!#! Arquivo salvo com sucesso #!#!#!\n')
                break
            else:
                print('\n!!! O arquivo precisa ter uma extensão .txt !!!\n')
                continue

    dadosAluno = Aluno(nome,endereco,dataNascimento,sexo,telefoneCelular,telefoneResidencial,email,estadoCivil,ra)
    dadosCurso = Curso('ADS','Noturno','2','10','500,00','Tecnólogo','Curso voltado para ...','Devops, banco de dados, python ...')
    dadosMatricula = Matricula('64758475796','10-04-2016')
    y = RegistrosAluno(dadosAluno,dadosCurso,dadosMatricula, nomeArquivo)
    y.salvarRegistrosAluno()

    while True: # repete a função validaDadosAluno
            repete = input('\nPara salvar dados de mais um aluno digite "1" ou "2" para sair\n')
            if len(repete) == 0:
                print('\n!!! esse campo não pode ser nulo !!!\n')
                continue
            if repete.isdecimal() != True:
                print('\n!!! Inválido, digite apenas 1 ou 2 !!!\n')
                continue
            if repete == '1':
                break
            elif repete == '2':
                exit()
            else:
                print('\n!!! Inválido !!!\n')
                continue



