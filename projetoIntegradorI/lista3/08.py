# 8) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.A. contendo 10 valores.

a = float(input('Digite um valor inicial: '))
r = float(input('Informe uma razão: '))

pa = [a]

for i in range(1, 10, 1):
  pa.append(a + (i * r))

print(pa)