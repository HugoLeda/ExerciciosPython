# Ler 5 valores numéricos em uma lista, inserindo-os na ordem crescente e correta na lista no momento da leitura, sem usar o comando sort().

def montarListaCrescente(qtdNumeros: int):
  lista = []

  for i in range(qtdNumeros):
    n = int(input('Digite um número: '))
    inserido = False # variável para controlar se o número digitado já foi inserido na lista

    if ( (lista == []) or (n >= max(lista)) ):
      lista.append(n)
      print(f'Como a lista está: {lista}')
    else:
      for j in range(len(lista)):
        if ( (n < lista[j]) and (inserido == False) ):
          restante = []

          for k in range(j, len(lista)): # armazenar os valores maiores que o valor n a ser inserido
            restante.append(lista[k])

          lista[j] = n
          inserido = True
          lista.append(0) 

          count = 0
          for l in range((j + 1), len(lista)): # reinserir os valores maiores que n na ordem correta          
            lista[l] = restante[count]
            count += 1
          
          print(f'Como a lista está: {lista}')

  return lista
      
numeros = montarListaCrescente(5)
print(numeros)