import random, webbrowser, time

def qualquerString():
    string = ''
    letras = 'ABCDEFGHIJMNOPQRSTUVWXYZ'
    string = random.choice(letras)
    for i in range(10):
        string += random.choice(letras.lower())
    return string

print('\nAperte "00" para sair a qualquer momento\n')
while True:
    print('\n Query gerada')
    print('\n'+ ('+---' * 7) + '+\n')
    variasDatas     = ['2010','2011','2012','2013','2014','2015','2016','2017','2018']
    complementosEmail = ['@hotmail.com','@gmail.com','@yahoo.com']
    ufs = ['Acre-AC','Alagoas-AL','Amapá-AP','Amazonas-AM','Bahia-BA','Ceará-CE','Distrito Federal-DF',
    'Espírito Santo-ES','Goiás-GO','Maranhão-MA','Mato Grosso-MT','Mato Grosso do Sul-MS','Minas Gerais-MG',
    'Pará-PA','Paraíba-PB','Paraná-PR','Pernambuco-PE','Piauí-PI','Rio de Janeiro-RJ','Rio Grande do Norte-RN',
    'Rio Grande do SulRS','Rondônia-RO','Roraima-RR','Santa Catarina-SC','São Paulo-SP','Sergipe-SE','Tocantins-TO']
    id_cliente = random.randint(1, 17)
    titulo = f"Nethoog.{random.choice(ufs)}"
    razao_social = f"Ackermann {titulo[8:]} Ltda. - ME."
    cnpj = f"0{random.randint(1, 9)}.{random.randint(100, 900)}.{random.randint(100, 900)}.0001-{random.randint(10, 90)}"
    id_tipo = random.randint(1, 6)
    cep = f"{random.randint(100, 999)}{random.randint(10, 99)}-{random.randint(100, 999)}"
    logradouro = qualquerString()
    numero = random.randint(10, 10000)
    complemento = qualquerString()
    bairro = qualquerString()
    estado = titulo[8:]
    telefone = f"{random.randint(10, 50)} {random.randint(1000, 5000)}-{random.randint(1000, 5000)}"
    ano      = random.choice(variasDatas)
    mes      = random.randint(1,12)
    dia      = random.randint(1,30)
    horas    = random.randint(0, 23)
    minutos  = random.randint(0, 59)
    segundos = random.randint(0, 59)

    if mes < 10:
        mes = str(mes)
        mes = f'0{mes}'
    else:
        mes = str(mes)
    if dia < 10:
        dia = str(dia)
        dia = f'0{dia}'
    else:
        dia = str(dia)
    if horas < 10:
        horas = str(horas)
        horas = f'0{horas}'
    else:
        horas = str(horas)
    if minutos < 10:
        minutos = f'0{minutos}'
    else:
        minutos = str(minutos)
    if segundos < 10:
        segundos = f'0{segundos}'
    else:
        segundos = str(segundos)

    criado_em = f'{ano}-{mes}-{dia} {horas}:{minutos}:{segundos}'

    content = (f'''insert into nethoog.tbl_clientes_locais values(null, {id_cliente},'{titulo}','{razao_social}','{cnpj}',
    {id_tipo},'{cep}','{logradouro}','{numero}','{complemento}','{bairro}', null, '{estado}', '{telefone}','{criado_em}', 'nao');\n''')
    arquivo = open('insert_into.sql','+a')
    arquivo.writelines(content)
    arquivo.close()

    print("\nContinua? s / n ")
    continua = input()
    if continua == "s":
        continue
    elif continua == "n":
        break
    else:
        exit()
webbrowser.open_new_tab('insert_into.sql')
time.sleep(1)
arquivo = open('insert_into.sql','w')
arquivo.close()
