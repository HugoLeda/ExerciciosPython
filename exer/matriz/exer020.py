# tendo uma matriz 5×5 preenchida com valores aleatórios entre 0 e 99,  mostre qual é o segundo maior valor existente na matriz.
import random

matriz = [0] * 5
maiorValor = -1000
segundoMaior = -1000

for i in range(5):
    matriz[i] = [0] * 5

for row in range(5):
    for collum in range(5):
        matriz[row][collum] = random.randint(0, 99)

for row in range(5):
    for collum in range(5):
        if (matriz[row][collum] >= maiorValor):
            maiorValor = matriz[row][collum]
        elif (matriz[row][collum] > segundoMaior):
            segundoMaior = matriz[row][collum]
        
print("Matriz: ", matriz, "\nMaior Valor: ", maiorValor, "\nSegundo maior valor: ", segundoMaior)        