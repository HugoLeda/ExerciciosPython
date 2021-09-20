# Faça um script que gere palpites para a loteria. O script deve perguntar quantos jogos serão gerados e sorteará 6 números de 1 a 60 para cada jogo, cadastrando tudo em uma lista composta. Mostre a lista composta gerada no final.

from random import randint

def gerarJogos(qtd: int):
  jogos = []

  for i in range(qtd):
    jogo = []
    
    for i in range(6):
      n = randint(1, 60)
      if (n not in jogo):
        jogo.append(n)
    
    jogos.append(jogo)

  return jogos

qtdJogos = int(input('Deseja gerar quantos jogos: '))
jogos = gerarJogos(qtdJogos)

for i in range(len(jogos)):
  print(f'Jogo {i + 1}: {jogos[i]}')