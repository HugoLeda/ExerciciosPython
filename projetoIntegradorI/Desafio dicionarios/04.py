# Ler nome, curso e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e o dicionário em uma lista. Mostre no final os dados de todas as pessoas tabulados, a quantidade de pessoas cadastradas, uma lista com os maiores de idade e uma lista com os menores de idade;

def printarLista(lista: list):
  for i in range(len(lista)):
    print(lista[i])

pessoas = []
maiores = []
menores = []

executar = True

while (executar):
  nome = input('Digite um nome: ')
  curso = input('Digite o curso: ')
  idade = int(input('Digite a idade: '))
  while (idade < 0):
    idade = int(input('Idade inválida, digite outra: '))
  
  pessoa = {"nome": nome, "curso": curso, "idade": idade}
  pessoas.append(pessoa)

  if (idade >= 18):
    maiores.append(pessoa)
  else:
    menores.append(pessoa)

  res = input('Deseja continuar [S/N]: ')
  if (res[0].upper() == 'N'):
    executar = False

print(f'\nPessoas cadastradas:')
printarLista(pessoas)
print(f'\nQuantidade de pessoas cadastradas: {len(pessoas)}')
print(f'\nMaiores de idade:')
printarLista(maiores)
print(f'\nMenores de idedade:')
printarLista(menores)