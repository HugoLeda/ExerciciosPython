# Visualização de dados crescimento da populção brasileira 1980-2016

import matplotlib.pyplot as plt

dados = open("popu.csv").readlines()

x, y = []

for i in range(len(dados)):
  if i != 0:
    linha = dados[i].split(";")
    x.append(int(linha[0]))
    y.append(int(linha[1]))

titulo = "Populção brasileira 1980-2016"
eixox = "Ano"
eixoy = "População brasileira (x⁷)"

plt.bar(x, y, color = "#ccc")
plt.plot(x, y, color = 'k', linestyle = "--")

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.savefig("09.png", dpi = 600)
plt.show()