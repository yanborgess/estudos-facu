arquivo = open('dados.txt', 'w')

for i in range(3):
    nomes =  str(input('Digite os nomes a serem cadastrados: '))
    arquivo.write(nomes+'\n')
arquivo.close()

arquivo = open('dados.txt', 'r')
nome = arquivo.readlines()


print(f'O segundo nome cadastrado foi: {nome[1]}')