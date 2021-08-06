# 6) Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.

numeros = []
for i in range(100, 200, 1):
  if ((i % 2) != 0):
    numeros.append(i)

print(f'Impares de 100 a 200: {numeros}')