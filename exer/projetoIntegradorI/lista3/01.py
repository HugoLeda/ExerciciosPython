# 1) Desenvolver um algoritmo que efetue a soma de todos os números pares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.

numeros = []
for i in range(1, 500, 1):
  par = i % 2
  if (par == 0):
    m3 = i % 3
    if (m3 == 0):
      numeros.append(i)

soma = 0
for i in numeros:
  soma += i

print(f'Números pares multiplos de 3: {numeros}\nSua soma: {soma}')