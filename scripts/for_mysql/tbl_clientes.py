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
    id_tipo = random.randint(1, 4)
    id_plano = random.randint(1, 2)
    nome_fantasia = qualquerString()
    razao_social = qualquerString() + '.Ltda'
    cnpj = f"0{random.randint(1, 9)}.{random.randint(100, 900)}.{random.randint(100, 900)}.0001-{random.randint(10, 90)}" #05.750.164.0001-50
    contato_nome = qualquerString()
    contato_email = f"{qualquerString()}{random.choice(complementosEmail)}"
    contato_telefone = f"{random.randint(10, 50)} {random.randint(1000, 5000)}-{random.randint(1000, 5000)}"
    contato_whatsapp = f"{random.randint(10, 50)} {random.randint(1000, 5000)}-{random.randint(1000, 5000)}"
    website = qualquerString() + '.com.br'

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

    content = (f"insert into nethoog.tbl_clientes values(null, {id_tipo}, {id_plano},'{nome_fantasia}', '{razao_social}','{cnpj}','{contato_nome}','{contato_email}', 1, '{contato_telefone}','{contato_whatsapp}','{website}','{criado_em}','nao');\n")
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
