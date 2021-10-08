# Faça um script que leia o NOME, as notas P1 e P2 de uma aluno. Calcule sua média aritmética e guarde além da média a situação do aluno (APROVADO ou REPROVADO) em um dicionário. Mostre a estrutura no final;

def situacaoAluno(nome: str, p1: int, p2: int):
  media = round((p1 + p2) / 2, 2)
  if (media >= 7 and media <= 10):
    res = 'APROVADO'
  elif (media < 7 and media > 0):
    res = 'REPROVADO'
  else:
    res = 'Notas inválidas'

  return {"aluno": nome, "Nota 1": p1, "Nota 2": p2, "Média": media, "Situacao": res}

qtd = int(input('Digite a quantidade de alunos que deseja registrar: '))

alunos = []

for i in range(qtd):
  nome = input('Digite o nome do aluno: ')
  p1 = int(input(f'Nota 1 de {nome}: '))
  p2 = int(input(f'Nota 2 de {nome}: '))
  
  alunos.append(situacaoAluno(nome, p1, p2))

for i in range(len(alunos)):
  print(alunos[i])