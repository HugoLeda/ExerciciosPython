# 7) Faça um algoritmo que leia uma variável e some 5, caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação

n = float(input('informe um número: '))

resto = n % 2

if (resto == 0):
  n += 5
else:
  n += 8

print(f'Resultado: {n}')