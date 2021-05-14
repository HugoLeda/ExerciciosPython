import matplotlib.pyplot as plt

x = ['1', '2', '3', '4']
y = ['1', '2', '3', '2']

plt.title('Primero Gráfico') #título do gráfico

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.plot(x, y)
plt.show()