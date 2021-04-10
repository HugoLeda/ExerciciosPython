# Author: João Hugo Leda
# faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 10 posições. Substitua todas as ocorrência de valores positivos por 1 e todos os valores negativos por 0.

i = 0
numbers = []

while i < 10:
    number = float(input("Digite o número %i: " %(i + 1)))
    numbers.append(number)
    i += 1

for j in range(10):    
    if (numbers[int(j)] > 0):
        numbers[int(j)] = 1
    elif (numbers[int(j)]  < 0):
        numbers[int(j)]  = 0

print(numbers)        