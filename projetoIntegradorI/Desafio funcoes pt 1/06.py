# Faça um script que tenha duas funções. A primeira irá sortear 10 números inteiros e guarda-lo em uma lista, a segunda irá contar a quantidade de pares na lista criada.

from random import randint

def sortearNumeros():
  numeros = []

  for i in range(10):
    numeros.append(randint(-1000, 1000))

  return numeros

def qtdPares(numeros: list):
  pares = 0

  for i in range(len(numeros)):
    if (numeros[i] % 2 == 0):
      pares += 1

  return pares

numeros = sortearNumeros()
pares = qtdPares(numeros)

print(f'Números: {numeros}\nQuantidade de pares: {qtdPares}')