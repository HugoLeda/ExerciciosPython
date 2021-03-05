pergunta  = "S"
while pergunta == "S":
    valor1 = float(input("Digite o valor 1: "))
    valor2 = float(input("Digite o valor 2: "))

    soma = valor1 + valor2
    print("%.2f + %.2f = %.2f" %(valor1, valor2, soma))

    pergunta = input("Novo Cálculo (S/N)?")
    pergunta = pergunta.upper()
print("Fim dos Cálculos!")