# Ler vários números para uma lista até que o usuário deseje. Depois criar mais duas listas: uma somente com os números pares e outra, somente com os números ímpares. Mostrar as 3 listas no final.

numeros = []
pares = []
impares = []

continuar = True
while (continuar == True):
  n = int(input('Digite um número: '))
  numeros.append(n)

  resp = input('Deseja continuar [S/N]: ')
  if (resp[0].upper() == 'N'):
    continuar = False

for i in numeros:
  if ((i % 2) == 0):
    pares.append(i)
  else:
    impares.append(i)

print(f'\nLista Completa: {numeros}\nPares: {pares}\nImpares: {impares}')