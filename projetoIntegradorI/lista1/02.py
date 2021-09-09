# 2. Faça um script em Python para calcular quantas ferraduras são necessárias para equipar todos os cavalos comprados para um haras.

qtdCavalos = int(input('Quantidade de cavalos comprados: '))

if (qtdCavalos < 0):
  print('Valor inváldo!')
else:
  qtdFerraduras = qtdCavalos * 4

  print(f'São necessária {qtdFerraduras} para equipar todos os cavalos')