matrix = []

for i in range(2):
    inteiros = []
    for i in range(3):
        num = int(input('Digite um numero inteiro: '))
        inteiros.append(num)
    matrix.append(inteiros)

pos = []

for inteiros in matrix:
    for num in inteiros:
        if num > 0:
            pos.append(num)
soma = sum(pos)

print(f'A soma de todos os valores positivos é igual a: {soma}')