#Visualização de dados
import matplotlib.pyplot as plt

x1 = [1,3,5,7,9]
y1 = [2,4,6,8,10]

x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]

titulo = "Gráfico de barras 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(titulo)

#eixos
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1,y1, label = "Grupo 1", color = "b")
plt.bar(x2,y2, label = "Grupo 2", color = "r")
plt.legend()
plt.show()