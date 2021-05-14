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
plt.plot(x,y, label = "Meus pontos", color = "b")
plt.legend()

plt.scatter(x,y, color = "r")
plt.legend()
plt.show()
