from allClasses import *

print('\n*Os dados do professor serão salvos em um arquivo\n')



dadosProfessor = Professor('João','rua antonio azevedo','10-06-4356','M','234324324-3432432','23432-32','C.TEDJKAS','CASADO','231231454')
disciplina = lecionaDisciplina('matematica')
dadosAcademicos = dadosAcademicos('banco de dados','doutor')
y = RegistrosProfessor(dadosProfessor,disciplina,dadosAcademicos,'testando.txt')
y.salvarRegistrosProfessor()


