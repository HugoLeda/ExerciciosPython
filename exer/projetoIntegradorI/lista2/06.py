# 6) Faça um programa em Python que leia a média de duas avaliações (P1 e P2). Calcule e mostre a média final do aluno. Calcule e mostre se o aluno foi APROVADO ou REPROVADO, sabendo que a média para aprovação deve ser maior ou igual a 7.

n1 = float(input('Informe a nota da P1 do aluno: '))
n2 = float(input('Informe a nota da P2 do aluno: '))

media = (n1 + n2) / 2

if (media >= 7):
  res = 'APROVADO'
else:
  res = 'REPROVADO'

print('O aluno foi:', res)