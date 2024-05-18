matrix = []

for i in range(3):
    prod = [] 
    for i in range(3):
        produtos = input('Digite o nome do produto: ')
        prod.append(produtos)
    matrix.append(prod)

linha = int(input('Digite a linha desejada [0][2]=> '))
coluna = int(input('Digite a coluna desejada [0][2]=> '))

linha_desejada = matrix[linha][coluna]

print(f'Produto na posição: ({linha}, {coluna}): {linha_desejada}')
