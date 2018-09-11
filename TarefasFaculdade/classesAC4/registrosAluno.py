from allClasses import * 

print('\n*Os dados do aluno serão salvos em um arquivo\n')

while True:
    #VALIDACOES ALUNO
    while True: #nome
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
    while True: #endereço
        endereco = input('Endereço: ').capitalize()
        if len(endereco) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        else:
            break
    while True: #data de nascimento
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
    while True: #sexo
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
    while True: #telefone celular
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
    while True: #telefone residencial
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
    while True: #e-mail
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
    while True: #estado civil
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
            break
    while True: #  RA
        ra = input('Ra: ')
        if len(ra) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if ra.isdecimal() == True and len(ra) == 7:
            break
        else:
            print('\n!!! Valor Inválido, o RA precisa ser um sequência de 7 números!!!\n')
            continue
    dadosAluno = Aluno(nome,endereco,dataNascimento,sexo,telefoneCelular,telefoneResidencial,email,estadoCivil,ra)
    # VALIDACOES CURSO
    while True: #nome curso
        try:
            nome = input('\nCurso: ').capitalize()
            if nome == '':
                print('\n!!! esse campo não pode ser nulo !!!\n')
                continue
            validaString = int(nome)
            print('\n!!! Valor Inválido !!!\n')
            continue
        except:
            break
    while True: #periodo
        listaPeriodo = ['diurno','noturno','matinal']
        periodo = input('Periodo: ').lower().replace(' ','')
        if periodo == 'x':
            exit()
        if len(periodo) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if periodo in listaPeriodo:
            periodo = periodo.capitalize()
            break
        else:
            print('\n!!! Inválido !!!\n')
            print('\n*opções disponíveis: Diurno, Noturno e Matinal\n')
            continue
    while True: #duracao
        duracao = input('Quantidade de semestres: ')
        if len(duracao) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if int(duracao) == 1:
            duracao = f'{duracao} Semestre'
            break
        elif int(duracao) > 1:
            duracao = f'{duracao} Semestres'
            break
        else:
            print('\n!!! Valor Inválido !!!\n')
            continue   
    while True: #notaMEC
        notaMEC = input('Nota MEC: ')
        if len(notaMEC) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if notaMEC.isdecimal() == True and int(notaMEC) >= 0 and int(notaMEC) <= 10:
            break
        else:
            print('\n!!! Valor Inválido !!!\n')
            continue
    while True: #valorMensalidade
        try:
            valorMensalidade = float(input('Valor Mensalidade: '))
        except ValueError:
            print('\n!!! Inválido, informe um número (exemplo 100 ou 250.00) !!!\n')
        else:
            valorMensalidade = f'R${valorMensalidade:.2f}'
            print(valorMensalidade)
            break
    while True: #tipo
        try:
            tipo = input('\nTipo: ').capitalize().replace(' ','')
            if tipo == '':
                print('\n!!! esse campo não pode ser nulo !!!\n')
                continue
            validaString = int(tipo)
            print('\n!!! Valor Inválido !!!\n')
            continue
        except:
            break
    while True: #descricao
        try:
            descricao = input('\nDescrição: ')
            if descricao == '':
                print('\n!!! esse campo não pode ser nulo !!!\n')
                continue
            if len(descricao) > 100:
                print('\n!!! A descrição precisa ter no máximo 100 caracteres !!!\n')
                continue
            validaString = int(descricao)
            print('\n!!! Valor Inválido !!!\n')
            continue
        except:
            break
    while True: #disciplinas
        try:
            disciplinas = input('\nDisciplinas: ')
            if descricao == '':
                print('\n!!! esse campo não pode ser nulo !!!\n')
                continue
            if len(disciplinas) > 100:
                print('\n!!! Esse campo pode ter no máximo 100 caracteres !!!\n')
                continue
            validaString = int(disciplinas)
            print('\n!!! Valor Inválido !!!\n')
            continue
        except:
            break
    dadosCurso = Curso(nome, periodo, duracao, notaMEC, valorMensalidade, tipo, descricao, disciplinas)
    # VALIDACOES MATRÍCULA
    while True: #número matrícula
        numeroMatricula = input('Número Matrícula: ')
        if len(numeroMatricula) == 0:
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if numeroMatricula.isdecimal() == True and len(numeroMatricula) == 10:
            break
        else:
            print('\n!!! Valor Inválido, o número da matrícula precisa ser um sequência de 10 números!!!\n')
            continue
    while True: #data
        dataMatricula = input('Data Matrícula (ex.14-07-1966): ')
        if dataMatricula == '':
            print('\n!!! esse campo não pode ser nulo !!!\n')
            continue
        if len(dataMatricula) != 10:
            print('\n!!! Valor Inválido !!!\n')
            continue
        contaHifen = dataMatricula.count('-')
        if contaHifen != 2:
            print('\n!!! Valor Inválido !!!\n')
            continue
        validaDataMatricula = dataMatricula.split('-')
        if len(validaDataMatricula) != 3:
            print('\n!!! Valor Inválido !!!\n')
            continue
        listaTamanho = []
        for i in validaDataMatricula:
            tamanhoElemento = len(i)
            listaTamanho.append(tamanhoElemento)
        if listaTamanho != [2,2,4]:
            print('\n!!! Valor Inválido !!!\n')
            continue
        contaErros = 0
        for i in validaDataMatricula:
            try:
                validaNumero = int(i)
            except:
                contaErros += 1
        if contaErros != 0:
            print('\n!!! Valor Inválido !!!\n')
            continue
        else:
            break
    dadosMatricula = Matricula(numeroMatricula,dataMatricula)
    while True: #nome do arquivo
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
    y = RegistrosAluno(dadosAluno,dadosCurso,dadosMatricula, nomeArquivo)
    y.salvarRegistrosAluno()
    while True: #repete a função validaDadosAluno
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
