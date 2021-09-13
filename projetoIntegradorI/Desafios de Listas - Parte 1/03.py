# Ler 5 valores numéricos em uma lista, inserindo-os na ordem crescente e correta na lista no momento da leitura, sem usar o comando sort().

lista = [0]

for i in range(5):
  n = int(input('Digite um número: '))

  for i in range(len(lista)):
    if (n < lista[i]):
      restante = []

      for j in range(i, len(lista)):
        restante.append(lista[j])

      lista[i] = n
      lista.append(0)

      for k in range((i + 1), len(lista)):
        lista[k] = restante[k - (i + 1)]
    else:
      lista.append(n)

print(lista)