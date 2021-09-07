# Gere uma tupla com 5 números inteiros aleatórios e exiba o maior e menor número gerado

import random

numeros = (
  random.randint(0, 50), 
  random.randint(0, 50), 
  random.randint(0, 50),
  random.randint(0, 50), 
  random.randint(0, 50)
)

maior = numeros[0] 
menor = numeros[0]
for i in numeros:
  if (menor > i):
    menor = i
  if (maior < i):
    maior = i

print(f'Maior número gerado: {maior}\nMenor número gerado: {menor}')