a = int(input("Digite o valor para a: "))
b = int(input("Digite o valor para b: "))

if a > b :
    resultado = a / b
else :
    resultado = b / a    

if (resultado // 1 == resultado): 
    print("São múltiplos!")
else :
    print("Não são múltiplos!")