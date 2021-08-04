# 8) Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.

n1 = int(input('Informe um valor inteiro: '))
n2 = int(input('Informe outro valor inteiro: '))
n3 = int(input('Informe outro valor inteiro: '))

if ((n1 != n2) and (n1 != n3) and (n2 != n3)):
  if (n1 > n2 and n1 > n3):
    maior = n1
    if (n2 > n3):
      medio = n2
      menor = n3
    else:
      medio = n3
      menor = n2

  elif (n2 > n1 and n2 > n3):
    maior = n2
    if (n1 > n3):
      medio = n1
      menor = n3
    else:
      medio = n3
      menor = n1

  elif (n3 > n1 and n3 > n2):
    maior = n3
    if (n1 > n2):
      medio = n1
      menor = n2
    else:
      medio = n2
      menor = n1

  print(maior, medio, menor)

else :
  print('Os números devem ser todos diferentes entre si!')