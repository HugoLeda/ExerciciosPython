# Melhore o desafio número 3, adaptando-o para vários times. Mostre no final: o nome do time, a quantidade de gols por partida e o saldo de gols de cada time em todo o campeonato.

def registrarTime():
  nome = input('Digite o nome da equipe: ')
  qtdJogos = int(input('Quantidade de partidas jogadas: '))
  
  totalGols = 0
  golsSofridos = 0
  gols = []
  golsS = []
  for i in range (qtdJogos):
    qtdGol = int(input(f'Digite a quantidade de gols marcados no jogo {i +  1}: '))
    golSofrido = int(input(f'Digite a quantidade de gols sofridos no jogo {i +  1}: '))
    
    while (qtdGol < 0):
      qtdGol = int(input(f'Digite a quantidade de gols marcados no jogo {i +  1}: '))

    while (golsSofridos < 0):      
      golSofrido = int(input(f'Digite a quantidade de gols sofridos no jogo {i +  1}: '))
    
    totalGols += qtdGol
    golsSofridos += golSofrido
    resJogoS = [i + 1, golSofrido]
    resJogo = [i + 1, qtdGol]
    gols.append(resJogo)
    golsS.append(resJogoS)

  saldo = totalGols - golsSofridos
  gols = dict(gols)
  equipe = {"nome": nome, "partidas": qtdJogos, "gols": gols, "total de gols": totalGols, "gols sofridos": golsS, "total gols sofridos": golsSofridos, "saldo": saldo}

  return equipe

dados = []

executar = True

while(executar):
  dados.append(registrarTime())

  res = input('Deseja continuar [S/N]: ')
  if (res[0].upper() == 'N'):
    executar = False

for i in range(len(dados)):
  print(dados[i])

executar = True

while(executar):
  res = input('Deseja ver o resultado de um time especifico: [S/N]: ')
  if (res[0].upper() == 'N'):
    executar = False
  elif (res[0].upper() == 'S'):
    param = input('Digite o nome: ')
    for i in range(len(dados)):
      if (dados[i]["nome"].upper() == param.upper()):
        print(dados[i])