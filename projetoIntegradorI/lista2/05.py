# 5) Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

n = float(input('Informe um número: '))

if (n > 0):
  res = n * 2
else:
  res = n * 3

print(f'Resultado: {res}')