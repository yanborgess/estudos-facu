matrix = []

for i in range(2):
    linha = []
    for i in range(2):
        altura = float(input('Digite a a altura em metros: '))
        linha.append(altura)
    matrix.append(linha)

contador = 0 

for linha in matrix:
    for altura in linha:
        if altura > 1.50:
            contador += 1 

print(f'A quantidade de pessoas com mais de 1.50m é igual a: {contador}')