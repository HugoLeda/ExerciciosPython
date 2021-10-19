# Faça uma função que calcule a área de um terreno retangular. A função deve receber como parâmetros a largura e comprimento do terreno.

from random import randint

def areaRetangulo(l: float, c: float):
  return round((l * c), 3)

l = randint(1, 100)
c = randint(1, 100)
area = areaRetangulo(l, c)
print(f'Largura: {l}m\nComprimento: {c}m\nÁrea: {area}m2')