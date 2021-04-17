# tendo uma matriz 10×10 preenchida com valores aleatórios entre 10 e 50,  mostre qual é o maior valor existente a matriz desconsiderando os  elementos da diagonal principal.
import random

matriz = [0] * 10 
maiorValor = -1000

for i in range(10):
    matriz[i] = [0] * 10

for row in range(10):
    for collum in range(10):         
        matriz[row][collum] = random.randint(10,50)

for row in range(10):
    for collum in range(10):
        if (row != collum):
            if(matriz[row][collum] > maiorValor):
                maiorValor = matriz[row][collum]

print(matriz, "\n", maiorValor)