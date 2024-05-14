idades = []
contador1 =  0
contador2 = 0 
contador3 = 0

for i in range(5):
    idade = int(input('Qual sua idade: '))
    idades.append(idade)

    if idade < 18: 
        contador1+=1 
    elif idade < 60:
        contador2 +=1 
    else:
        contador3 += 1 
    media = sum(idades) / 5 

print(f'''
A quantidade de pessoas com menos de 18 anos é igual a: {contador1}
entre 18 é 60 anos: {contador2}
acima de 60 anos: {contador3}
e a média de idades de todos é igual a: {media}
''')