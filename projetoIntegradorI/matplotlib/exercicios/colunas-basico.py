from matplotlib import pyplot as plt

dados = ["Amoroso", "Bebeto", "Dodô", "Denilson", "Ronaldo"]
gols = [3, 3, 4, 5, 2]

plt.bar(dados, gols, color = "yellow")

plt.xlabel("JOGADORES")
plt.ylabel("QUANTIDADE DE GOLS")
plt.title("ARTILHEIROS DA RODADA", c = "blue")

plt.show()