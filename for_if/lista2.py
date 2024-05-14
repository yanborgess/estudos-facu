masc = []
fem = []

print('''
           QUAL SEU SEXO:
            [1] MASCULINO
            [2] FEMININO 
                   ''')

for i in range(3):
    sexo = int(input('Qual seu sexo: '))

    if sexo == 1:
        masc.append(sexo)
    elif sexo ==  2:
        fem.append(sexo)

print('a quantidade de cada sexo são:\n masculino:',len(masc),'\n feminino:',len(fem))