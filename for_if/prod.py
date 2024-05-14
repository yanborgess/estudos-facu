precos = []

for i in range(10):
    preco = float(input(f'Digite os valores dos produtos {i +1 }: '))
    precos.append(preco)

maior_preco = max(precos)
print(f"O produto mais caro custa R$ {maior_preco:.2f}")


