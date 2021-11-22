import matplotlib.pyplot as plt

x = ['Santos', 'Corinthians', 'São Paulo', 'Palmeiras']
y = [8, 7, 6, 6]

titulo = "Títulos Brasileiros"
eixox = "Clube"
eixoy = "Títulos"

plt.title(titulo)

#eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y)
plt.show()