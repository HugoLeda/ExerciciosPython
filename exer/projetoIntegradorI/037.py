# 37. Faça um script em Python que calcule e mostre a tabuada de um número digitado pelo usuário.

n = float(input('Digite um número para ver sua tabuada: '))

print('\n*** Tabuada ***\n')
for i in range(11):
  valor = n * i
  print(f'{i} * {n} = {valor}')

print('\nFim!!!')