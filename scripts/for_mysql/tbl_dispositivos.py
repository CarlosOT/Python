import random, webbrowser, time

print('\nAperte "00" para sair a qualquer momento\n')
while True:
    print('\n Query gerada')
    print('\n'+ ('+---' * 7) + '+\n')
    tiposDisp = ['mobile','desktop']
    tipoDispositivo = random.choice(tiposDisp)
    numeros = '1234567890'
    letras = 'ABCDEFGHIJMNOPQRSTUVWXYZ'
    macAdress = ''
    for i in range(3):
      macAdress += f"{random.choice(numeros)}{random.choice(letras)}:{random.choice(letras)}{random.choice(numeros)}"
      if i < 2:
          macAdress += ':'
    ip = f"{random.randint(100, 130)}."
    for i in range(4):
        ip += f"{random.randint(0,9)}"
        if i < 3:
            ip += '.'
    variosOs = ['mac os','Android','Windows 8.1','Ubuntu 18','Windows 10','Linux Mint','Windows XP']
    os = random.choice(variosOs)
    variosBrowsers = ['Google Chrome','Safari','Mozilla Firefox','Internet Explorer','Microsoft Edge']
    browser = random.choice(variosBrowsers)
    variasDatas = ['2010-07-09','2011-05-04','2012-03-06','2013-06-02','2014-03-02','2015-01-01','2016-12-11','2017-08-09','2018-09-08']
    variosHorarios = ['00:12:23','22:45:23','17:04:12','09:54:12','23:12:12','20:40:00','19:10:50','10:06:13','06:48:45']
    criado_em = f"{random.choice(variasDatas)} {random.choice(variosHorarios)} "
    content = (f"insert into nethoog.tbl_dispositivos values(null,'{tipoDispositivo}','{macAdress}','{ip}','{os}','{browser}', null, 'nao','{criado_em}', null);\n")
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
