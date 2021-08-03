# 1) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.

a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))

if ((a + b) > c):
  print('Soma de A + B é maior que C')
else:
  print('Soma de A + B é não maior que C')