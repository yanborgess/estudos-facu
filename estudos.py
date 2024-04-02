def CalculaMedia(n1,n2):
    media = (n1+n2)/2
    print(f'A media entre {n1} e {n2} é igual a : ', media)

def calculaprod(n1,n2):
    prod = (n1*n2)
    print(f'O produto entre {n1} é {n2} é igual a : ',prod)

def calculadiv(n1,n2):
    div = n1 / n2 
    print(f'A divisão entre {n1} e {n2} é igual a :',div)

def subn1(n1,n2):
    sub = n1 - n2
    print(f'A subtraçao entre {n1} e {n2} e igual a :',sub)

def subn2(n1,n2):
    sub2 = n2 - n1
    print(f'A subtraçao entre {n1} e {n2} e igual a :',sub2)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('Opções:        Operação:')
print('    1            Media entre os números ')
print('    2            Diferença do maior pelo menor ')
print('    3            Produto entre os números digitados')
print('    4            Divisão do primeiro pelo segundo')

op = int(input('Digite a operação desejada: '))

if op == 1:
    CalculaMedia(n1,n2)

if op == 2:
    if n1 > n2:
        subn1(n1,n2)
    elif n2 > n1:
        subn2(n1,n2)
    else:
        print('Eles são iguais! A diferença e 0!')

if op == 3:
    calculaprod(n1,n2)

if op ==4:
    calculadiv(n1,n2)













