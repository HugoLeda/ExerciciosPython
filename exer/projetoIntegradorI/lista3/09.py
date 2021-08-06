# 9) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.G. contendo 10 valores.

a = float(input('Digite um valor inicial: '))
r = float(input('Informe uma razão: '))

pg = [a]

for i in range(1, 10, 1):
  pg.append(pg[i - 1] * r)

print(pg)