#Visualização de dados
import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,7,1,0]

titulo = "Scatterplot: Gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)

#eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x,y, color = "#990000", linestyle = ':')

plt.scatter(x, y, label = "Meus pontos", color = "g", marker = ".", s = 200)
plt.legend()
plt.show()
