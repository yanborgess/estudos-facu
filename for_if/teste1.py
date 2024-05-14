print ('---- ESCOLHA UMA OPÇAO ----')
print('     01 |  REGULAR        ')
print('     02 |  BOM            ')
print('     03 |  ÓTIMO          ')
print ('----------------------------')

cont1 = 0
cont2 = 0
cont3 = 0

for i in range(5):
    op = int(input(f'Digite sua opnião sobre o filme: '))
    
    if op == 1:
        cont1 += 1
    elif op == 2:
        cont2 += 1
    else: 
        cont3 += 1

print(f'\n{cont1} acharam o filme regular!! ')
print(f'{cont2} acharam o filme bom!!')
print(f'{cont3} acharam o filme ótimo!!')


