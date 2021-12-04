from matplotlib import pyplot as plt
import numpy as np

diaSemana = ["S", "T", "Q", "Q", "S"]
homens = [9, 6, 9, 8, 5]
mulheres = [6, 8, 9, 6, 7]

x1 = np.arange(len(homens))
x2 = [x + 0.25 for x in x1]

plt.bar(x1, mulheres, width=0.25, label="MULHERES", color="pink")
plt.bar(x2, homens, width=0.25, label="HOMENS", color="blue")

plt.xticks([x + 0.25 for x in range(len(mulheres))], diaSemana)

plt.ylabel("TOTAL DE ALUNOS NO DIA")
plt.xlabel("DIAS DA SEMANA ANALISADOS")
plt.title("FREQUÊNCIA DOS ALUNOS NA SEMANA")
plt.legend()

plt.show()