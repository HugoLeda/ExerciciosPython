# 2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar : a. A menor altura do grupo; b. A maior altura do grupo;

alturas = []
for i in range (14):
  alt = float(input(f'Informe a altura {i}: '))
  alturas.append(alt)

menor = alturas[0]
maior = alturas[0]

for i in range(len(alturas)):
  if (menor > alturas[i]):
    menor = alturas[i]
  if (maior < alturas[i]):
    maior = alturas[i]

print(f'Alturas informadas: {alturas}\nMaior altura informada: {maior}\nMenor altura informada: {menor}')