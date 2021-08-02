# 18. A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra. Faça um script em Python para calcular e imprimir o salário bruto e o salário líquido de um determinado funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos

totalHoras = int(input('Informe o número de horas trabalhadas: '))
totalHorasExtras = int(input('Informe o número de horas extras trabalhadas: '))

if (totalHoras > 0 and totalHorasExtras >= 0):
  salBrt = (totalHoras * 10) + (totalHorasExtras * 15)
  salLiq = salBrt - (salBrt * 0.1)
  print('Salário Bruto:', salBrt, '\nSalário Liquido:', salLiq)
else:
  print('Verifique os valores informados!')