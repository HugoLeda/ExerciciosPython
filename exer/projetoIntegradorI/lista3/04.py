# 4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo.

numeros = []

n = 0
while (n >= 0):
  n = int(input('Digite um número: '))
  numeros.append(n)

intervalos = {'0-25': 0, '26-50': 0, '51-75': 0, '76-100': 0}

for i in numeros:
  if ((i >= 0) and (i <= 25)):
    intervalos['0-25'] += 1
  elif ((i >= 26) and (i <= 50)):
    intervalos['26-50'] += 1
  elif ((i >= 51) and (i <= 75)):
    intervalos['51-75'] += 1
  elif ((i >= 76) and (i <= 100)):
    intervalos['76-100'] += 1
  
print(intervalos)