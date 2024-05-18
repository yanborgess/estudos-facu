matrix = []

for i in range(3):
    reais = []
    for i in range(2):
        num = int(input('Digite algum numero real: '))
        reais.append(num)
    matrix.append(reais)

pos = []
neg = 0 

for reais in matrix:
    for num in reais:
        if num < 0:
            neg+=1 
        else:
            pos.append(num)
soma = sum(pos)

print(f'A quantidade de numeros negativos é igual a: {neg}')
print(f'A soma dos numeros positivos é igual a: {soma}')
