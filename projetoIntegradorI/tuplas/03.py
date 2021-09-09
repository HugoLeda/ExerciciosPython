# Montar uma tupla que contenha o nome e a nota de alunos (5 anos). Mostrar os dados de forma tabulada e a média final da sala toda

alunos = []
for i in range(5):
  aluno = []
  nome = input('Digite o nome de um aluno: ')
  nota = int(input(f'Digite a nota do aluno {nome}: '))
  aluno.append(nome)
  aluno.append(nota)
  alunos.append(aluno)

alunosTupla = tuple(alunos)
media = 0
soma = 0

for i in range(len(alunosTupla)):
  soma += alunosTupla[i][1]

media = round(soma / len(alunosTupla), 2)
print(f'Notas dos alunos: \n{alunosTupla}\n \nMédia Final da sala toda: {media}')