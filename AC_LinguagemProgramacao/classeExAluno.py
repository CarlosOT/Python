from classePessoa import Pessoa

class ExAluno(Pessoa):
    def __init__(self,nome, sobrenome, dataNasc, nacionalidade,anoFormacao,cursoConcluido, frequenciaEscolar, comportamento,pegouDP):
        Pessoa.__init__(self,nome, sobrenome, dataNasc, nacionalidade)
        self.anoFormacao = anoFormacao
        self.cursoConcluido = cursoConcluido
        self.frequenciaEscolar = frequenciaEscolar
        self.comportamento = comportamento
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
        print(f'\nNome: {self.nome} {self.sobrenome} / Nascimento: {self.dataNasc} / Nacionalidade: {self.nacionalidade}')
        print(f'Curso concluído: {self.cursoConcluido} / Nota Comportamento: {self.comportamento} / Frequência: {self.frequenciaEscolar}% / Pegou DP: {self.pegouDP} / Ano formação: {self.anoFormacao}')




nome = input('nome: ')
sobrenome = input('sobrenome: ')
dataNasc = input('Data Nascimento: ')
nacionalidade = input('Nacionalidade')
anoFormacao = input('Ano formação: ')
cursoConcluido = input('Curso concluído: ')
frequenciaEscolar = input('Frequência escolar: ')
comportamento = input('Comportamento: ')
pegouDP = input('Pegou DP: ')

z = ExAluno(nome, sobrenome, dataNasc, nacionalidade,anoFormacao,cursoConcluido, frequenciaEscolar, comportamento,pegouDP)

z.LancarNotasExAluno()
z.imprimeBoletimExAluno()
z.ImprimirDadosCompletos()
