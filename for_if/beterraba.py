print('-----VOCE GOSTA DE BETERRABA?------')
print('         OPÇÃO 1  I   SIM          ')
print('         OPÇAO 2  I   NÃO          ')
print('------------------------------------')

contpos = 0 
contneg = 0

for i in range(15):
    op = int(input('DIGITE A OPÇÃO: '))

    if op == 1:
        contpos += 1
    else:
        contneg += 1

print(f'A quantidade de pessoas que gostam são {contpos}, \n e os que não gostam são {contneg}')