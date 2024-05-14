#CALCULADORA BASICA


def calsoma(n1,n2):
    soma = n1 + n2
    print(f'A soma entre {n1} e {n2} é igual a: ',soma)

def calsub(n1,n2):
    sub = n1 - n2
    print(f'A subtração entre {n1} e {n2} é igual a: ', sub)

def caldiv(n1,n2):
    div = n1 / n2 
    print(f'A dvisao entre {n1} e {n2} e igual a: ', div)

def calmult(n1,n2):
    mult = n1 * n2 
    print(f'A multiplicaçao entre {n1} e {n2} e igual a :',mult)



n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

print('----------------------------------------------')
print('        ESCOLHA A OPERAÇÃO DESEJADA:          ')
print('----------------------------------------------')
print('                SOMA               |    1      ')
print('                SUBTRAÇÃO          |    2      ')
print('                DIVISÃO            |    3      ')
print('                MULTIPLICAÇÃO      |    4      ')
print('----------------------------------------------')

op = int(input('OPÇÃO: '))

if op == 1:
    calsoma(n1,n2)

elif op == 2:
    calsub(n1,n2)

elif op == 3:
    caldiv(n1,n2)

elif op == 4:
    calmult(n1,n2)
