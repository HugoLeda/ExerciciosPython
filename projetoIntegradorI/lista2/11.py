# 11) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.

#Código Condição de pagamento

#1 À vista em dinheiro ou cheque, recebe 10% de desconto
#2 À vista no cartão de crédito, recebe 15% de desconto
#3 Em duas vezes, preço normal de etiqueta sem juros
#4 Em três vezes, preço normal de etiqueta mais juros de 10%

preco = float(input('Informe o preço do produto: '))
pag = int(input('Informe o código de pagamento: '))

if (pag == 1):
  preco -= preco * 0.1
elif (pag == 2):
  preco -= (preco * 0.15)
elif (pag == 3):
  preco = preco
elif (pag == 4):
  preco += preco * 0.1
else:
  print('Código de pagamento inválido!')

print(f' Valor a ser pago: {round(preco, 2)}')