valor = []
contador4 = 0 
contador5 = 0 
contador8 = 0 

for i in range(5):
    prod =  float(input('Qual valor do produto? '))
    valor.append(prod)
    if prod < 49.99:
        contador4 += 1
    elif prod < 80.00:
        contador5 += 1 
    else:
        contador8 +=1 
    
    media = sum(valor)/5

print(f'''
A quantidade de produtos inferior a R$50.00 é igual a: {contador4}
inferior a R$80.00: {contador5}
acima de R$100.00: {contador8}
e a média entre eles é igual a: {media:.2f}
''')
    
    