i = 0
soma = 0

pergunta = input("Digitar um número? (S/N)? ")
pergunta = pergunta.upper()

while pergunta == "S":
    i = i + 1
    numero = float(input("Digite um número: "))

    soma = soma + numero

    pergunta = input("Digitar novo número? (S/N)? ")    
    pergunta = pergunta.upper()

print("%i números digitados que somados resultam em %.2f" %(i, soma)) 