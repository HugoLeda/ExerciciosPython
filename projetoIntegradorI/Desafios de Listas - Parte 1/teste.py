# Ler 5 valores numéricos em uma lista, inserindo-os na ordem crescente e correta na lista no momento da leitura, sem usar o comando sort().

lista = []

for i in range(5):
  n = int(input('Digite um número: '))
  inserido = False

  if ( (lista == []) or (n > max(lista)) ):
    lista.append(n)
  else:
    for j in range(len(lista)):
      if ( (n < lista[j]) and (inserido == False) ):
        restante = []

        for k in range(j, len(lista)):
          restante.append(lista[k])

        lista[j] = n
        inserido = True
        lista.append(0) 

        temp = 0
        for l in range((j + 1), len(lista)):          
          lista[l] = restante[temp]
          temp += 1
      
print(lista)