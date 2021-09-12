# Ler vários valores para uma lista. Ao ler um número já existente dentro da lista, este deve ser rejeitado. Fazer isto até o usuário desejar. No final, exibir a lista lida em ordem crescente.

lista = []

def verificarElemento(lista: list, el: int):
  for i in lista:
    if (el == i):
      return True
  return False

def ordenarLista(lista: list):
  
  for i in range(len(lista) - 1, 0, -1):
    for j in range(i):
      if (lista[j][1] > lista[j + 1][1]):
        temp = lista[j]
        lista[j] = lista[j + 1]
        lista[j + 1] = temp

  return lista

continuar = True
while (continuar == True):
  n = int(input('Digite um número: '))

  while (verificarElemento(lista, n)):
    n = int(input('Elemnto ja inserido! Digite outro: '))

  lista.append(n)
  resp = input('Deseja continuar [S/N]: ')

  if (resp[0].upper() == 'N'):
    continuar = False

lista = ordenarLista(lista)
print(f'Números digitados em ordem crescente: {lista}')