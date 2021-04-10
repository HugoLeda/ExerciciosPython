#tendo uma matriz 10×10 preenchida com valores aleatórios entre 10 e 50, mostre a média dos elementos da diagonal secundária.
import random

matriz = [0] * 10

for i in range(10):
    matriz[i] = [0] * 10

for row in range(10):
    for collum in range(10):         
        matriz[row][collum] = random.randint(10,50)

aux = 9
soma = 0

for i in range(10):
    soma += matriz[i][aux]
    aux -= 1

soma = soma/10

print("Média da diagonal secundária: %.2f" %(soma))