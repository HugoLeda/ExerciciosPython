# 7. Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano. Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.

diaAtual = int(input('Informe o dia: '))
mesAtual = int(input('Informe o mês: '))

totalDias = ((mesAtual - 1) * 30) + diaAtual

print('Se passaram ', totalDias, ' dias desde 01 - 01 até', diaAtual, '-', mesAtual)