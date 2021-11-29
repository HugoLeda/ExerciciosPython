from matplotlib import pyplot as plt

meses = ["MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET"]
watts = [80, 40, 80, 110, 180, 120, 240]

plt.plot(meses, watts, marker = "o")
plt.xlabel("MESES")
plt.ylabel("WATTS")
plt.title("CONSUMO DE ENERGIA (W)")

plt.show()