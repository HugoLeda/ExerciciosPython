from matplotlib import pyplot as plt

massaCorporal = [72, 80, 60, 90, 100, 120, 82, 79, 78, 55, 71, 75, 130, 105, 60, 54, 58, 57, 60, 62]
alturaCM = [180, 170, 175, 174, 185, 190, 182, 179, 165, 165, 170, 169, 177, 173, 172, 162, 163, 167, 171, 181]

plt.scatter(massaCorporal, alturaCM, c = "green")

plt.xlabel("MASSA MUSCULAR (KG)")
plt.ylabel("ALTURA (CM)")
plt.title("MASSA MUSCULAR VERSUS ALTURA")
plt.tick_params(axis='both')

plt.show()