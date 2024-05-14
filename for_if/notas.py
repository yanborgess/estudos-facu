nota = []
repro = 0 
final = 0 
apro = 0 

for i in range(5):
    notas = float(input('Quais foram as notas: '))
    nota.append(notas)
     
    if notas < 4.9:
        repro += 1 
    elif notas < 7.0:
        final+=1 
    else: 
        apro+= 1 
    media = sum(nota) / 5

print(f'''
A quantidade de alunos com nota inferior a 5.0 é igual a: {repro} e estão REPROVADOS 
entre 7.0 e 5.0: {final} e estão na PROVA FINAL 
acima de 7.0:  {apro} e estão APROVADOS
e a média dos alunos é igual a: {media}
''')
