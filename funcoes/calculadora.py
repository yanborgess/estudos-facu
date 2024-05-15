from funcoes import soma,subtracao,mult,div


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
    soma(n1,n2)

elif op == 2:
    subtracao(n1,n2)

elif op == 3:
    div(n1,n2)

elif op == 4:
    mult(n1,n2)