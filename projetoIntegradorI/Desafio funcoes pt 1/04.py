# Faça uma função que receba como parâmetros o inicio, o fim e o passo. Gere todos os números entre o inicio e fim de acordo com o passo. Suponha que inicio e fim sempre serão diferentes e o passo pode ser positivo ou negativo.

from random import randint

def gerarNumeros(start: int, stop: int, step: int):
  numeros = []
  for i in range(start, stop, step):
    numeros.append(i)
  return numeros

print(gerarNumeros(randint(0, 100), randint(0, 100), randint(-10, 10)))