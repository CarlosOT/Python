from classeAluno import Aluno

class ExAluno(Aluno):
    def __init__(self,nome, sobrenome, dataNasc, nacionalidade, RA, curso, notaComportamento, frequenciaEscolar, anoFormacao, pegouDP):
        Aluno.__init__(self,nome, sobrenome, dataNasc, nacionalidade, RA, curso,notaComportamento, frequenciaEscolar)
        self.anoFormacao = anoFormacao
        self.frequenciaEscolar = frequenciaEscolar
        self.pegouDP = pegouDP
        self.materia = ''
        self.NotasExAluno = []
        self.boletimExAluno = {}
        self.mediaExAluno = ''

    def LancarNotasExAluno(self):

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
                    self.NotasExAluno.append(nota)
                    contador += 1

                def mediaExAluno():
                    soma = sum(self.NotasExAluno)
                    elementos_lista = len(self.NotasExAluno)
                    media = soma / elementos_lista
                    self.mediaExAluno = media
                mediaExAluno()

                self.boletimExAluno[self.materia] = self.mediaExAluno

    def imprimeBoletimExAluno(self):
        print('\nMatérias / Médias\n')
        for key, value in self.boletimExAluno.items():
            print(f'{key} - {value:.2f}')

    def ImprimirDadosCompletos(self):
        print(f'\nNome: {self.nome} {self.sobrenome}\nNascimento: {self.dataNasc}\nNacionalidade: {self.nacionalidade}')
        print(f'Curso concluído: {self.curso}\nRa: {self.RA}\nNota Comportamento: {self.notaComportamento}')
        print(f'Frequência: {self.frequenciaEscolar}%\nPegou DP: {self.pegouDP}\nAno formação: {self.anoFormacao}')




nome = input('nome: ')
sobrenome = input('sobrenome: ')
dataNasc = input('Data Nascimento: ')
nacionalidade = input('Nacionalidade: ')
RA = input('RA: ')
curso = input('Curso concluído: ')
notaComportamento = input('Nota Comportamento: ')
frequenciaEscolar = input('Frequência escolar: ')
anoFormacao = input('Ano formação: ')
pegouDP = input('Pegou DP: ')

z = ExAluno(nome, sobrenome, dataNasc, nacionalidade, RA, curso, notaComportamento, frequenciaEscolar, anoFormacao, pegouDP)

z.LancarNotasExAluno()
z.imprimeBoletimExAluno()
z.ImprimirDadosCompletos()
