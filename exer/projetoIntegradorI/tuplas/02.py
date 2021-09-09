# Ler 5 números inteiros para uma tupla e mostre a quantidade de pares, ímpares e zeros

qtdZeros = 0
qtdPares = 0
qtdImpares = 0

n = []
for i in range(5):
  x = int(input('Digite um número: '))
  n.append(x)

numeros = tuple(n)

for i in numeros:
  if (i == 0):
    qtdZeros += 1
  elif ((i % 2) == 0):
    qtdPares += 1
  else:
    qtdImpares += 1

print(f'Tupla: {numeros}\nQuantidade de Pares: {qtdPares}\nQuantidade de Zeros: {qtdZeros}\n Quantidade de ímpares: {qtdImpares}')