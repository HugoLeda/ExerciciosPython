# 12) Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de aproveitamento, usando a fórmula:

#MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7

#A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E.

#Média de aproveitamento Conceito

#>= 9.0 A
#>= 7.5 e < 9.0 B
#>= 6.0 e < 7.5 C
#>= 4.0 e < 6.0 D
#< 4.0 E

ni = int(input('Informe o número de identificação: '))
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
me = float(input('Informe a média dos exercícios: '))

ma = (n1 + (n2 * 2) + (n3 * 3) + me) / 7

if (ma >= 9):
  conceito = 'A'
  res = 'Aprovado'
elif (ma >= 7.5 and ma < 9):
  conceito = 'B'
  res = 'Aprovado'
elif (ma >= 6 and ma < 7.5):
  conceito = 'C'
  res = 'Aprovado'
elif (ma >= 4 and ma < 6):
  conceito = 'D'
  res = 'Reprovado'
else:
  conceito = 'E'
  res = 'Reprovado'

print(f'Número do aluno: {ni}\nNota 1: {n1}\nNota 2: {n2}\nNota 3: {n3}\nMédia dos exercícios: {round(me, 2)}\nMédia de aproveitamento: {round(ma, 2)}\nConceito: {conceito}\nResultado: {res}')