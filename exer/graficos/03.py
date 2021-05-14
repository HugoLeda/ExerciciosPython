#Visualização de dados
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,7,1,4]

titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)

#eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y)
plt.show()
