# Faça um script que gere automáticamente a jogada (resultados aleatórios) de 6 jogadores de dados (resultados de 1 a 6) e que guarde estes resultados em um dicionário. Mostre, no final, o dicionário ordenado em ordem decrescente e mostrando a classificação de cada jogador;

from random import randint

def ordenarJogadores(jogadores: list):
  for i in range(len(jogadores) - 1, 0, -1):
    for j in range(i):
      if (jogadores[j][1] > jogadores[j + 1][1]):
        temp = jogadores[j]
        jogadores[j] = jogadores[j + 1]
        jogadores[j + 1] = temp
  return jogadores

resultados = {}
jogadores = []

for i in range(6):
  nome = input('Digite o nome do jogador: ')
  
  while (nome in resultados):
    nome = input('Jogador já resgistrado, insira outro nome: ')
  
  resultado = randint(1, 6)
  resultados[nome] = resultado
  jogador = [nome, resultado]
  jogadores.append(jogador)

  print(f'Jogardor: {nome}\nPontos: {resultado}\n')

jogadores = ordenarJogadores(jogadores)
resultados = dict(jogadores)
print(resultados)