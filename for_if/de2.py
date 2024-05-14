


prod = float(input('Digite o do produto: '))

if prod <= 50:
    print('O valor do produto com aumento de 5% é igual a : ', (prod *5/100)+prod)
elif prod <=100: 
    print('O valor do produto com aumentode 10% é igual a: ', (prod *10/100)+prod)
else:
    print('o valor do produto com aumento de  15% é igual a: ',(prod *15/100)+prod)

if prod <= 80:
    print('O produto escolhido é barato!!')
elif prod <=120:
    print('O produto escolhi é um valor normal!! ')
elif prod <=200:
    print('O produto escolhido é caro!!!')
else:
    print('O produto é muito caro!!!')