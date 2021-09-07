# 13. Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma: CENTENA = x; DEZENA = x, UNIDADE = x

n = int(input('Digite um número inteiro com três digitos: '))

if (len(str(n)) == 3):
  c = str(n)[0]
  d = str(n)[1]
  u = str(n)[2]

  print('Centena =', c, '\nDezena =', d, '\nUnidade =', u)
else:
  print('Valor inválido!')