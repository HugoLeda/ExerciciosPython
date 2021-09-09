# 6. O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um script em Python que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.

pesoPrato = float(input('Informe o peso do prato (em Kg): '))

if (pesoPrato < 0):
  print('Peso inválido!')
else:
  valorPagar = pesoPrato * 12
  print(f'Valor a pagar: R$ {valorPagar}')