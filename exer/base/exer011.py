i = 0
result = 0

while i < 10 :
    n = float(input("Digite o número %i: " %(i + 1)))
    if n > result :
        result = n

    i += 1

print("O maior número digitado foi: %.2f" %(result))