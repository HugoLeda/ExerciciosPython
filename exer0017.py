# faça um algoritmo que solicite ao usuário números e os armazene em uma matriz 6×6. Em seguida, crie um vetor ue armazene os elementos da diagonal principal da matriz.

matriz = [0] * 6
vetor = [0] * 6

for i in range(6):
    matriz[i] = [0] * 6

for row in range(6):
    for collum in range(6):
        matriz[row][collum] = int(input("Digite um valor inteiro: "))

for row in range(6):  
    for collum in range(6):
        if(row == collum):
            vetor[collum] = matriz[row][collum]

print(matriz)            
print(vetor)