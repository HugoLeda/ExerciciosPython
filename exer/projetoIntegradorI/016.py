# 16. A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um script em Python em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra.

qtdSand = int(input('Quantidade de sanduíches a fazer: '))

pesoPres = (qtdSand * 50) / 1000
pesoQuei = (qtdSand * 50 * 2) / 1000
pesoHamb = (qtdSand * 100) / 1000

print(f'Serão necessários:\n', pesoPres, 'Kg de preseunto\n', pesoQuei, 'Kg de queijo\n', pesoHamb, 'Kg de hamburguer')