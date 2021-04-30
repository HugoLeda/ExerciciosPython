"""
crie um algoritmo que leia um valor e a partir disso faça:
(1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;
(2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número;
(3) se for os valores 6, 7 e 8, mostre o valor dividido 9.
"""
import math

def tratarValor(n) :
  n = int(n)
  if (type(n) == int) :
    if (n > 0 and n <= 3) :
      return n * n
    elif (n == 4 or n == 9) :
      return math.sqrt(n)
    elif (n >= 6 and n <= 8) :
      return n/9
    else :
      return "Entre com um valor de 1 à 9!"
  else :
    return "ERRO: Essa função deve receber valores numéricos!"

valor = input('Digite um número: ')
valor = tratarValor(valor)
print("Seu número tratado é: ", valor)