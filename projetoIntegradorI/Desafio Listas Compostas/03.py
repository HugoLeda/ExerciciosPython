# Faça um script que leia uma matriz 2 X 2 de números inteiros. Mostre no final a matriz em formatação correta (forma de matriz).

matriz = [[], []]

for i in range(2):
  for j in range(2):
    n = int(input(f'Digite o elemento {i + 1}{j + 1}: '))
    matriz[i].append(n)

print('Matriz 2x2: ')
for i in range(len(matriz)):
  print(matriz[i])