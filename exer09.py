i = 0

pergunta = input("Digitar um número? (S/N)?")
pergunta = pergunta.upper()

while pergunta == "S":
    i = i + 1
    numero = input("Digite um número: ")

    pergunta = input("Digitar novo número? (S/N)?")    
    pergunta = pergunta.upper()

print("%i números digitados" %(i)) 