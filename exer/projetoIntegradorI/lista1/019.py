# 19. A granja Frangotech possui um controle automatizado de cada frango da sua produção. No pé direito do frango há um anel com um chip de identificação; no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50, faça um script em Python para calcular o gasto total da granja para marcar todos os seus frangos.

qtdFrangos = int(input('Informe a quantidade total de frangos: '))

if (qtdFrangos > 0):
  gasto = (qtdFrangos * 4) + (qtdFrangos * 3.5)
  print(f'O gasto total será de: R$ {gasto}')
else:
  print('Quantidade inválida!')