from classePessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self,nome, sobrenome, dataNasc, nacionalidade, RA, curso,notaComportamento, frequenciaEscolar):
        Pessoa.__init__(self,nome,sobrenome,dataNasc,nacionalidade)
        self.RA = RA
        self.curso = curso
        self.materia = ''
        self.notaComportamento = notaComportamento
        self.frequenciaEscolar = frequenciaEscolar
        self.listaNotas = []
        self.media = ''
        self.boletim = {}

    def LancarNotasAluno(self):

        validacaoDisciplina = True
        while validacaoDisciplina:
            try:
                disciplinas = int(input('\nQuantidade de Disciplinas a cadastrar: ')) 
                validacaoDisciplina = False 
            except:
                print('opção inválida')

        validacaoQtdeNotas = True
        while validacaoQtdeNotas:
            try:
                qtde_notas = int(input('Quantidade de notas a cadastrar: '))
                validacaoQtdeNotas = False
            except:
                print('opção inválida')

        for iteracao_discplina in range(disciplinas):

            self.materia = input('\nMatéria: ')

            contador = 0
            while contador < qtde_notas:
                try:
                    nota = int(input('nota: '))
                except:
                    print('opção inválida')
                    continue

                if nota < 0 or nota > 10:
                    print('opção inválida')
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

                self.boletim[self.materia] = self.media

    def imprimeBoletim(self):
        print('\nMatérias / Médias\n')
        for key, value in self.boletim.items():
            print(f'{key} - {value:.2f}')

    def imprimeDadosAluno(self):
        print(f'\nNome: {self.nome} {self.sobrenome} / Nascimento: {self.dataNasc} / {self.nacionalidade}')
        print(f'Curso: {self.curso} / RA: {self.RA} / Nota Comportamento: {self.notaComportamento} / Frequência: {self.frequenciaEscolar}%')
                    
    



nome = input('\nNome do aluno: ')
sobrenome = input('Sobrenome: ')
data_nascimento = input('Data nascimento: ')
Nacionalidade = input('Nacionalidade: ')
RA = input('RA: ')
curso = input('Curso: ')
notaComportamento = input('Nota comportamento: ')
frequenciaEscolar = input('Frequência: ')


x = Aluno(nome, sobrenome, data_nascimento, Nacionalidade, RA, curso,notaComportamento, frequenciaEscolar)
x.LancarNotasAluno()
x.imprimeDadosAluno()
x.imprimeBoletim() 


