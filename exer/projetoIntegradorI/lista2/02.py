# 2) Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

nome = input('Informe seu nome: ')
sexo = input('Informe o sexo: ')
es = input('Informe o estado civil: ')
tc = ''

sexo = sexo[0].upper()
es = es.upper()

if (sexo == 'F' and es == 'CASADA'):
  tc = int(input('Informe o tempo de casada: '))

if (tc != ''):
  print(f'\nNome: {nome}\nSexo: {sexo}\nEstado Civil: {es}\nTempo de Casada: {tc}')
else:
  print(f'Nome: {nome}\nSexo: {sexo}\nEstado Civil: {es}')