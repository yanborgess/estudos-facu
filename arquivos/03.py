
for i in range(3):
    nome_arquivo =  input('Digite o nome do arquivo desejado a ser criado: ')
    arquivo = open(f'{nome_arquivo}.txt', 'w')
    nome = str(input('Digite seu nome: '))
    numero =  input('Digite seu numero: ')
    arquivo.write(nome+'\n')
    arquivo.write(numero+'\n')
arquivo.close()

