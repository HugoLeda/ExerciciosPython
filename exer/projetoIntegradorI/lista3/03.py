# 3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos.

import numpy as np

numeros = []

continuar = True
while (continuar == True):
  n = float(input('Digite um valor: '))
  numeros.append(n)
  res = input('Deseja digitar mais números [S/N]: ')
  res = res[0].upper()
  if (res == 'N'):
    continuar = False

media = np.mean(numeros)

qtdPositivos = 0
qtdNegativos = 0
for i in numeros:
  if (i > 0):
    qtdPositivos += 1
  elif (i < 0):
    qtdNegativos += 1

percPositivos = (100 / len(numeros)) * qtdPositivos 
percNegativos = (100 / len(numeros)) * qtdNegativos

print(f'Valores lidos: {numeros}\nMédia dos valores: {media}\nQuantidade de valores positivos: {qtdPositivos}\nQuantidade de valores negativos: {qtdNegativos}\nPercentual de positivos: {percPositivos} %\nPercentual de negativos: {percNegativos} %')