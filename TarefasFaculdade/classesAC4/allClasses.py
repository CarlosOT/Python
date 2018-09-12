class Pessoa:
    def __init__(self, nome, endereco, dataNascimento, sexo, telefoneCelular, telefoneResidencial, email, estadoCivil):
        self.nome = nome
        self.endereco = endereco
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.telefoneCelular = telefoneCelular
        self.telefoneResidencial = telefoneResidencial
        self.email = email
        self.estadoCivil = estadoCivil
class Aluno(Pessoa):
    def __init__(self, nome, endereco, dataNascimento, sexo, telefoneCelular, telefoneResidencial, email, estadoCivil, ra):
        Pessoa.__init__(self, nome, endereco, dataNascimento, sexo, telefoneCelular, telefoneResidencial, email, estadoCivil)
        self.ra = ra
class Curso:
    def __init__(self, nome, periodo, duracao, notaMEC, valorMensalidade, tipo, descricao, disciplinas):
        self.nome = nome
        self.periodo = periodo
        self.duracao = duracao
        self.notaMEC = notaMEC
        self.valorMensalidade = valorMensalidade
        self.tipo = tipo
        self.descricao = descricao 
        self.disciplinas = disciplinas
class Matricula:
    def __init__(self, numero, data):
        self.numero = numero
        self.data = data
class RegistrosAluno:
    def __init__(self, dadosAluno, dadosCurso, dadosMatricula, nomeArquivo):
        self.aluno = dadosAluno
        self.curso = dadosCurso
        self.matricula = dadosMatricula
        self.nomeArquivo = nomeArquivo
    def salvarRegistrosAluno(self):
        arquivo = open(self.nomeArquivo,'+a')

        aluno = (f'Nome: {self.aluno.nome}\nEndereço: {self.aluno.endereco}\nData Nascimento: {self.aluno.dataNascimento}')
        arquivo.write(aluno)
        aluno = (f'Sexo: {self.aluno.sexo}\nTelefone Celular: {self.aluno.telefoneCelular}\nTelefone Residencial: {self.aluno.telefoneResidencial}')
        arquivo.write(aluno)
        aluno = (f'Email: {self.aluno.email}\nEstado Civil: {self.aluno.estadoCivil}\nRA: {self.aluno.ra}')
        arquivo.write(aluno)
        curso = (f'Curso: {self.curso.nome}\nPeríodo: {self.curso.periodo}\nDuraçao: {self.curso.duracao}')
        arquivo.write(curso)
        curso = (f'Nota Mec: {self.curso.notaMEC}\nValor Mensalidade: {self.curso.valorMensalidade}\nTipo: {self.curso.tipo}\nDescrição: {self.curso.descricao}')
        arquivo.write(curso)
        matricula = (f'Número Matrícula: {self.matricula.numero}\nData: {self.matricula.data}')
        arquivo.write(matricula)
        arquivo.close()
class Professor(Pessoa):
    def __init__(self, nome, endereco, dataNascimento, sexo, telefoneCelular, telefoneResidencial, email, estadoCivil, registro):
        Pessoa.__init__(self, nome, endereco, dataNascimento, sexo, telefoneCelular, telefoneResidencial, email, estadoCivil)
        self.registro = registro
class Leciona:
    def __init__(self, disciplina):
        self.disciplina = disciplina
class dadosAcademicos:
    def __init__(self, especialidade, posicaoAcademica):
        self.especialidade = especialidade
        self.posicaoAcademica = posicaoAcademica
class RegistrosProfessor:
    def __init__(self, dadosProfessor, disciplina, dadosAcademicos, nomeArquivo):
        self.professor = dadosProfessor
        self.lecionaDisciplina = disciplina
        self.dadosAcademicos = dadosAcademicos
        self.nomeArquivo = nomeArquivo

    def salvarRegistrosProfessor(self):
        arquivo = open(self.nomeArquivo,'+a')
        professor = (f'Nome: {self.professor.nome}\nEndereço: {self.professor.endereco}\nData Nascimento: {self.professor.dataNascimento}')
        arquivo.write(professor)
        professor = (f'Sexo: {self.professor.sexo}\nTelefone Celular: {self.professor.telefoneCelular}\nTelefone Residencial: {self.professor.telefoneResidencial}')
        arquivo.write(professor)
        professor = (f'Email: {self.professor.email}\nEstado Civil: {self.professor.estadoCivil}\nNúmero de Registro: {self.professor.registro}')
        arquivo.write(professor)
        disciplina = (f'Disciplina: {self.lecionaDisciplina.disciplina}\n')
        arquivo.write(disciplina)
        dadosAcademicos = (f'Especialidade: {self.dadosAcademicos.especialidade}\nPosição Acadêmica: {self.dadosAcademicos.posicaoAcademica}')
        arquivo.write(dadosAcademicos)
        arquivo.close()
