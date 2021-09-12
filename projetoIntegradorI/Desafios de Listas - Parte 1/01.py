# Ler 5 valores em uma lista. Mostrar no final o menor e o maior valor lido.

lista = []

for i in range(5):
  n = int(input('Digite um valor: '))
  lista.append(n)

menor = lista[0]
maior = lista[0]

for i in lista:
  if (i < menor):
    menor = i
  if (i > maior):
    maior = i

print(f'Lista digitada: {lista}\nMaior valor: {maior}\nMenor valor: {menor}')