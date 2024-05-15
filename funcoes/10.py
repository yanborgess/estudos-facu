from funcoes import media2, diferenca, produto, div2

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo numero: '))

print('''
        ESCOLHA A OPÇAO 
      
    MEDIA ENTRE ELES -> 1 
    DIFERENÇA ->  2
    PRODUTO -> 3 
    DIVISÃO -> 4 
''')

op = int(input('Digite a operação desejada: '))

if op == 1:
    media2(n1,n2)
elif op == 2:
    diferenca(n1,n2)
elif op == 3:
    produto(n1,n2)
else:
    div2(n1,n2)



    
    
