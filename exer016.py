i = 0
numbers = []

def setValue(value):
    if (value > 0) and (value < 10):
        return 1
    elif (value >= 10):
        return 2
    else:    
        return 0

while i < 10:
    number = float(input("Digite o número %i: " %(i + 1)))
    numbers.append(number)
    i += 1

for j in range (len(numbers)):
    numbers[int(j)] = setValue(numbers[int(j)])

print(numbers)