# Faça um script que leia 10 números inteiros para uma lista composta (por 3 listas internas) que mantenha separados os números positivos, negativos e os números neutros. No final mostre todas as sub-listas em ordem crescente.

def ordenarLista(lista: list):
  
  for i in range(len(lista) - 1, 0, -1):
    for j in range(i):
      if (lista[j] > lista[j + 1]):
        temp = lista[j]
        lista[j] = lista[j + 1]
        lista[j + 1] = temp
        
  return lista

numeros = [[], [], []]
for i in range(10):
  n = int(input('Digite um número: '))
  if (n < 0):
    numeros[0].append(n)
  elif (n == 0):
    numeros[1].append(n)
  else:
    numeros[2].append(n)

for i in range(len(numeros)):
  numeros[i] = ordenarLista(numeros[i])

print(f'Negativos: {numeros[0]}\nNeutros: {numeros[1]}\nPositivos: {numeros[2]}')