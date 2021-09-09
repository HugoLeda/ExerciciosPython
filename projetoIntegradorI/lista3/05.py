# 5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero.

import numpy as np

print('Para encerrar digite 0!\n')

numeros = []

n = 1
while (n != 0):
  n = int(input('Digite um número positivo: '))
  while (n < 0):
    n = float(input('É necessário digitar um número positivo, por favor digite novamente: '))
  if (n != 0):
    numeros.append(n)  

pares = []
impares = []

for i in numeros:
  if ((i % 2) == 0):
    pares.append(i)
  else:
    impares.append(i)

mediaGeral = np.mean(numeros)
mediaPar = np.mean(pares)
mediaImpar = np.mean(impares)

print(f'Números digitados: {numeros}\nMédia dos números: {mediaGeral}\nQuantidade de números pares: {len(pares)}\nMédia dos números pares: {round(mediaPar, 2)}\nQuantidade de números ímpares: {len(impares)}\nMédia dos números ímpáres: {round(mediaImpar, 2)}')