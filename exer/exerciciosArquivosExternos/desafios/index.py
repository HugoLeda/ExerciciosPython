'''Faça um programa para alterar uma das notas de
um aluno.
O programa deve ter uma função que recebe o nome
do aluno, a nota velha e a nova nota. A função deve
fazer a alteração no arquivo.'''

data = [['João', 8], ['Rafa', 10], ['Lavinia', 10], ['Natan', 10]]

def alterarNota(aluno, nota):
  for i in range(len(data)):
    if (aluno == data[i][0]):
      data[i][1] = int(nota)
    else:
      return 'Aluno não encontrado!'
  return

alterarNota('João', 10)
print(data)