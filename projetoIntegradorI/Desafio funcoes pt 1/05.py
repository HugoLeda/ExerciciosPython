# Faça uma função que leia n números inteiros e mostre o maior e menor número digitados.

def lerNumeros():
  n = int(input('Digite a quantidade que deseja: '))
  numeros = []
  
  for i in range(n):
    numero = int(input('Digite um número: '))  
    numeros.append(numero)

  maior = numeros[0]
  menor = numeros[0]

  for i in numeros:
    if (i > maior):
      maior = i
    elif (i < menor):
      menor = i
    
  return {"maior": maior, "menor": menor}

print(lerNumeros())