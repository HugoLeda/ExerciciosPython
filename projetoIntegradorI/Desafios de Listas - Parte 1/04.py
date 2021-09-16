# Ler vários números em uma lista até que o usuário deseje. Exibir no final: a quantidade de números digitados, a lista em ordem decrescente e a quantidade de pares e ímpares.

def ordenarLista(lista: list):
  
  for i in range(len(lista) - 1, 0, -1):
    for j in range(i):
      if (lista[j] < lista[j + 1]):
        temp = lista[j]
        lista[j] = lista[j + 1]
        lista[j + 1] = temp
        
  return lista

numeros = []

continuar = True
while (continuar == True):
  n = int(input('Digite um número: '))
  numeros.append(n)

  resp = input('Deseja continuar [S/N]: ')
  if (resp[0].upper() == 'N'):
    continuar = False

qtdPares = 0
qtdImpares = 0
numeros = ordenarLista(numeros)
print(f'Números digitados: {numeros}\nQuantidade de números: {len(numeros)}\nQuantidade de Números Pares: {qtdPares}\nQuantidade de números ímpares: {qtdImpares}')
