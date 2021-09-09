# Montar uma tupla com 5 palavras. Exibir no final as vogais e a quantidade de vogais de cada palavra

palavras = []
for i in range(5):
  p = input('Digite uma palavra: ')
  palavras.append(p)

p = tuple(palavras)
palavra = []
qtdvogal = []
vogais = []

for i in p:
  vogal = 0

  for j in i:
    l = j.upper()
    if (l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U'):
      vogal += 1
      vogais.append(j)

  palavra.append(i)
  qtdvogal.append(vogal)

print(f'Palavras {p}')
print(f'Vogais em sequência: {vogais}')
print(f'Palavras e suas quantidade de vogais: ')
for i in range(len(palavra)):
  print(f'  {palavra[i]}: {qtdvogal[i]}')