#  Faça um script que leia o nome e a idade de várias pessoas em uma lista composta. No final mostre quantas pessoas foram cadastradas, uma listagem (em tela) com os maiores de idade e uma listagem com os menores de idade (mostrando de forma tabular o nome e a idade).

def registrarPessoas(qtd: int):  
  pessoas = []

  for i in range(qtd):
    pessoa = []

    nome = input('Digite um nome: ')
    idade = int(input('Digite a idade: '))
    
    while (idade < 0):
      idade = int(input('Idade inválida: digite novamente: '))
    
    pessoa.append(nome)
    pessoa.append(idade)
    pessoas.append(pessoa)
  
  return pessoas

def separarIdade(pessoas: list):
  maiores = []
  menores = []
  

  for i in range(len(pessoas)):
    if (pessoas[i][1] >= 18):
      maiores.append(pessoas[i])
    else:
      menores.append(pessoas[i])

  res = {'maiores': maiores, 'menores': menores}
  return res

pessoas = registrarPessoas(3)
print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
pessoas = separarIdade(pessoas)
maiores = pessoas['maiores']
menores = pessoas['menores']

print('Maiores de Idade:')
for i in range(len(maiores)):
  print(f'{maiores[i][0]}: {maiores[i][1]}')

print(f'Menores de Idade:')
for i in range(len(menores)):
  print(f'{menores[i][0]}: {menores[i][0]}')