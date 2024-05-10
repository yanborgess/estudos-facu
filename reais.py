pos = []
neg = []

for i in range(4):
    num = float(input('Digite qualquer numero: '))
    
    if num < 0:
        neg.append(num)
    else:
        pos.append(num)
    
    resultado = sum(pos)

print('A quantidade de numeros negativos na lista é igual a: ',len(neg))
print('A soma dos numeros positivos na lista é igua a: ',resultado)