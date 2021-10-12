# .Faça uma função que receba n valores (usando o desempacotador *) e exiba a soma dos valores.

from random import randint

def soma(valores: list):
  x, *restante = valores
  soma = x
  
  for i in range(len(restante)):
    soma += restante[i]

  return soma

print(soma([randint(-100, 100), randint(-100, 100), randint(-100, 100), randint(-100, 100)]))