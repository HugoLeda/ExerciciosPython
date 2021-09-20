# Leia o nome, a nota P1 e a nota P2 dos alunos do curso de ciências de dados, guardando tudo em uma lista composta. No final mostre todos os dados dos alunos e sua média final calculada (mostre em forma de tabela). Permita também mostrar as notas de cada aluno individualmente.

def registrarAlunos(qtd: int):
  alunos = []
  
  for i in range(qtd):
    aluno = []

    nome = input('Nome do aluno: ')
    p1 = int(input(f'Nota P1 de {nome}: '))
    p2 = int(input(f'Nota P2 de {nome}: '))
    media = (p1 + p2) / 2

    aluno.append(nome)
    aluno.append(p1)
    aluno.append(p2)
    aluno.append(media)

    alunos.append(aluno)

  return alunos

def exibirAlunos(alunos: list):
  print(f'*** Indice ***   ***  Aluno  ***     *** P1 ***   *** P2 ***   *** Média ***')
  for i in range(len(alunos)):
    print(f'     {i}                 {alunos[i][0]}                 {alunos[i][1]}                {alunos[i][2]}            {alunos[i][3]}')

alunos = registrarAlunos(3)
exibirAlunos(alunos)
mostrarAluno = input('Deseja ver as notas individuais de um aluno? [S/N]: ')

if (mostrarAluno[0].upper() == 'S'):
  indice = int(input('Digite o indice do aluno desejado: '))

for i in range(len(alunos)):
  if (i == indice):
    print(f'{alunos[i][0]}, P1: {alunos[i][1]}, P2: {alunos[i][2]}, Média: {alunos[i][3]}')