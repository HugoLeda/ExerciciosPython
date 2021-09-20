# Faça um script que leia uma matriz 2 X 2 de números inteiros. Mostre no final: a soma de todos os números, a soma dos valores da segunda coluna e o maior número da primeira linha.

matriz = [[], []]
somaEl =0

for i in range(2):
  for j in range(2):
    n = int(input(f'Digite o elemento {i + 1}{j + 1}: '))
    matriz[i].append(n)
    somaEl += n

somaCol2 = 0
maiorLin1 = matriz[0][0]

for i in range(len(matriz)):
  somaCol2 += matriz[i][1]

for i in range(len(matriz[0])):
  if (matriz[0][i] > maiorLin1):
    maiorLin1 = matriz[0][i]

print(f'Soma de todos elementos: {somaEl}\nSoma da segunda coluna: {somaCol2}\nMaior número da primeira linha: {maiorLin1}')