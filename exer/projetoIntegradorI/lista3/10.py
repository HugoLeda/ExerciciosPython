# 10) Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

a = int(input('Digite um número para ver seu fatorial: '))
res = a
sequencia = ''

while(a > 0):
  if (a != 1):
    res = res * (a - 1)    
    sequencia = sequencia + f'{a} X '
  else:
    sequencia = sequencia + f'{a}'
  a -= 1

print(sequencia, '=', res)