# 9) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

# ● para homens: (72.7 * h) – 58;

# ● para mulheres: (62.1 * h) – 44.7.

def pesoIdeal(s: chr, h: float):
  if (s == 'F'):
    res = round((62.1 * h) - 44.7, 3)
  elif (s == 'M'):
    res = round((72.7 * h) - 58, 3)
  else:
    res = 'Sexo inválido, não foi possível calcular!'
  return res

sexo = input('Informe o sexo: ')
sexo = sexo[0].upper()
altura = float(input('Informe a altura em metros: '))

pi = pesoIdeal(sexo, altura)

print(f'Altura: {altura}\nSexo: {sexo}\nPeso Ideal: {pi}')