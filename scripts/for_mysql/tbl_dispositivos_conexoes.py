import random, webbrowser, time

print('\nAperte "00" para sair a qualquer momento\n')
while True:
    print('\n Query gerada')
    print('\n'+ ('+---' * 7) + '+\n')
    IdsAccessPoints = [1,7,8]
    variosStatus    = ['acessou_portal_cativo','codigo_validado','conectou','conectou_facebook','conectou_google','conectou_linkedin','conectou_instagram','conectou_autologin']
    variasDatas     = ['2010','2011','2012','2013','2014','2015','2016','2017','2018']

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
        
    data_hora_conexao = f'{ano}-{mes}-{dia} {horas}:{minutos}:{segundos}'
    id_dispositivo = random.randint(1, 22)
    id_access_point = random.choice(IdsAccessPoints)
    status = random.choice(variosStatus)
    tempo_conexao = random.randint(1, 140)
    
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

    content = (f"insert into nethoog.tbl_dispositivos_conexoes values(null,'{id_dispositivo}','{id_access_point}','{status}', null, null, '{data_hora_conexao}', null,'{tempo_conexao}','{criado_em}');\n")
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
