# 3. A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um script em Python para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.

qtdPaes = int(input('Quantidade de pães vendidos no dia: '))
qtdBroas = int(input('Quantidade de broas vendidas no dia: '))

valorTotal = 0
valorTotal = qtdPaes * 0.12
valorTotal += qtdBroas * 1.5

valorPopupanca = valorTotal * 0.1

print(f'Valor vendido no dia: R$ {valorTotal} \nValor para guardar na poupança: R$ {valorPopupanca}')