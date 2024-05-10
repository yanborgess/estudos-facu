bom = []
otimo = []
regular = []

print('''
    QUAL SUA OPNIÃO SOBRE O FILME 
        [1] BOM
        [2] OTIMO 
        [3] REGULAR    
            ''')

for i in range(5):
    op = int(input('DIGITE SUA OPNIÃO: '))

    if op == 1:
        bom.append(op)
    elif op == 2:
        otimo.append(op)
    else:
        regular.append(op)
 
print('A quantidade de votos são - \nBOM:', len(bom), '\nOTIMO: ',len(otimo), '\nREGULAR:',len(regular))
   