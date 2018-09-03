from classeAluno import Aluno

class AlunoRepetente(Aluno):
    def __init__(self,nome, sobrenome, dataNasc, nacionalidade, RA, curso,notaComportamento,frequencia,semestreReprovado):
        Aluno.__init__(self,nome, sobrenome, dataNasc, nacionalidade, RA, curso,notaComportamento, frequencia)
        self.reforcoMaterias = {}
        self.materiaReprovada = ''
        self.materiasReprovadas = {}
        self.semestreReprovado = semestreReprovado
        self.listaNotas = []
    
    def LancarNotasRepetente(self):

        while True:
            try:
                disciplinas = int(input('\nQuantidade de Disciplinas a cadastrar: '))
                break
            except:
                print('\n!!! Inválido !!!\n')
                continue
        while True:
            try:
                qtde_notas = int(input('Quantidade de notas a cadastrar: '))
                break
            except:
                print('\n!!! Inválido !!!\n')
                continue

        for iteracao_discplina in range(disciplinas):

            while True:
                try:
                    self.materiaReprovada = input('\nMatéria reprovada: ')
                    if len(self.materiaReprovada) == 0:
                        print('\n!!! A materia reprovada não pode ser vazia !!!\n')
                        continue
                    validaString = int(self.materiaReprovada)
                    print('\n!!! A materia reprovada não pode ser um número inteiro !!!\n')
                    continue
                except:
                    break

            contador = 0
            while contador < qtde_notas:
                try:
                    nota = int(input('nota: '))
                except:
                    print('\n!!! Inválido !!!\n')
                    continue

                if nota < 0 or nota > 10:
                    print('Nota precisa ser maior que 0 e menor que 10')
                    continue

                elif nota > 6:
                    print('Todas as notas de um repetente são menores ou iguais a 6')
                    continue

                else:
                    self.listaNotas.append(nota)
                    contador += 1

                def mediaAluno():
                    soma = sum(self.listaNotas)
                    elementos_lista = len(self.listaNotas)
                    media = soma / elementos_lista
                    self.media = media
                mediaAluno()

                self.materiasReprovadas[self.materiaReprovada] = self.media

    def imprimaMateriasReprovacao(self):
        print('\nMatérias Reprovadas / Médias\n')
        for key, value in self.materiasReprovadas.items():
            print(f'{key} - {value:.2f}')

    def PrecisaReforco(self):
        indice = 0
        print('\nMatérias para reforço:')
        for c in self.materiasReprovadas.keys():
            indice += 1
            print(f'{indice} - {c}')
            

    def imprimeDadosRepetente(self):
        print(f'Semestre reprovado: {self.semestreReprovado}\n')
        print(f'Nome: {self.nome} {self.sobrenome} / Nascimento: {self.dataNasc} / {self.nacionalidade}')
        print(f'Curso: {self.curso} / RA: {self.RA} / Nota Comportamento: {self.notaComportamento} / Frequência: {self.frequencia}%')

while True:
    try:
        nome = input('Nome do aluno Repetente: ')
        if len(nome) == 0:
            print('\n!!! Nome não pode ser vazio !!!\n')
            continue
        validaString = int(nome)
        print('\n!!! Nome não pode ser número inteiro !!!\n')
        continue
    except:
        break
while True:
    try:
        sobrenome = input('Sobrenome do aluno Repetente: ')
        if len(sobrenome) == 0:
            print('\n!!! Sobrenome não pode ser vazio !!!\n')
            continue
        validaString = int(sobrenome)
        print('\n!!! Sobrenome não pode ser número inteiro !!!\n')
        continue
    except:
        break
while True:
    try:
        data_nascimento = input('Data nascimento: ')
        if len(data_nascimento) == 0:
            print('\n!!! Data de nascimento não pode ser vazia !!!\n')
            continue
        validaInteiro = int(data_nascimento)
        break
    except:
        print('\n!!! Data de nascimento precisa ter apenas números e não pode ser caractere !!!\n')
        continue
while True:
    try:
        Nacionalidade = input('Nacionalidade: ')
        if len(Nacionalidade) == 0:
            print('\n!!! Nacionalidade não pode ser vazio !!!\n')
            continue
        validaString = int(Nacionalidade)
        print('\n!!! Nacionalidade não pode ser número inteiro !!!\n')
        continue
    except:
        break
while True:
    try:
        RA = input('RA: ')
        if len(RA) == 0:
            print('\n!!! O RA não pode ser vazio !!!\n')
            continue
        validaInteiro = int(RA)
        break
    except:
        print('\n!!! O RA não pode ser caractere !!!\n')
        continue
while True:
    try:
        curso = input('Curso: ')
        if len(curso) == 0:
            print('\n!!! O curso não pode ser vazio !!!\n')
            continue
        validaString = int(curso)
        print('\n!!! O curso não pode ser número inteiro !!!\n')
        continue
    except:
        break
while True:
    try:
        notaComportamento = input('Nota comportamento: ')
        if len(notaComportamento) == 0:
            print('\n!!! A nota de comportamento não pode ser vazia !!!\n')
            continue
        validaInteiro = int(notaComportamento)
        break
    except:
        print('\n!!! A nota de comportamento não pode ser um caractere !!! \n')
        continue
while True:
    try:
        frequencia = input('Frequência: ')
        if len(frequencia) == 0:
            print('\n!!! A frequência nas aulas não pode ser vazia !!!\n')
            continue
        validaInteiro = int(frequencia)
        break
    except:
        print('\n!!! A frequência nas aula não pode ser um caractere !!!\n')
        continue
while True:
    try:
        semestreReprovado = input('Semestre reprovado: ')
        if len(semestreReprovado) == 0:
            print('\n!!! O semestre reprovado não pode ser vazio !!!\n')
            continue
        validaInteiro = int(semestreReprovado)
        break
    except:
        print('\n!!! O semestre reprovado não pode ser um número inteiro !!!\n')



'''
y = AlunoRepetente(nome, sobrenome, data_nascimento, Nacionalidade, RA, curso,notaComportamento, frequencia, semestreReprovado)


y.LancarNotasRepetente()
y.imprimeDadosRepetente()
y.imprimaMateriasReprovacao()
y.PrecisaReforco()
'''












    
        

