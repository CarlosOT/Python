import random, webbrowser, time

print('\nAperte "00" para sair a qualquer momento\n')
while True:
    print('\n Query gerada')
    print('\n'+ ('+---' * 7) + '+\n')
    nome = ''
    letras = 'ABCDEFGHIJMNOPQRSTUVWXYZ'
    nome = random.choice(letras)
    for i in range(8):
        nome += random.choice(letras.lower())
    complementosEmail = ['@hotmail.com','@gmail.com','@yahoo.com']
    email = ''
    email = random.choice(letras)
    for i in range(8):
        email += random.choice(letras.lower())
    email = email + random.choice(complementosEmail)
    variosCpf = ['3243564758','23453647','3245364758','324356475','2132453647','12324536475','3243564736746','312453647','132453364','12435476235']
    cpf = random.choice(variosCpf)
    variosCnpj = ['2435675689767','43546576876','2324536547','12356487586','124364758','124356475869','12343647586','1323546475','13243567']
    cnpj = random.choice(variosCnpj)
    variasSenhas = ['123423tegdfh6','32453645udhft','43w546e5urdhgtd7','e56e57et54sg','132456345wyrge46','32435647eysrf','q34564ters5','245rfr54']
    senha = random.choice(variasSenhas)
    listaData = ['1978-12-01','1990-10-03','1967-10-04','1989-08-09','1950-03-01','1980-11-05','1987-08-08','1995-01-06']
    data_nascimento = random.choice(listaData)
    variosSexo = ['feminino','masculino','outro']
    sexo = random.choice(variosSexo)
    variosCelulares = ['11 32453647','12 32453647','13 143253465','14 324536436','13 42335647','15 134253656','16 23543474','17 235436476']
    celular = random.choice(variosCelulares)
    variosCep = ['23435645','324546456','4354664','3245346','23453647','14236475','890797865','43546758','23564758','324536748']
    cep = random.choice(variosCep)
    OrigemCad = ['facebook','portal','google','linkedin','instagram']
    origemCadastro = random.choice(OrigemCad)
    DataCriacao = ['2018-10-08','2017-09-09','2016-03-04','2015-07-01','2014-07-05','2013-04-02','2010-02-04']
    criado_em = random.choice(DataCriacao)
    content = (f"insert into nethoog.tbl_usuarios values(null,'{nome}','{email}','{cpf}','{cnpj}','{senha}','{data_nascimento}','{sexo}','{celular}','{cep}','{origemCadastro}','{criado_em}');\n")
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
