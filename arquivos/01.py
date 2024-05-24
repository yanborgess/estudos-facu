arquivos = open('Dados.txt' , 'w');

for i in range(3):
  nomes =  str(input('Digite o nome a ser cadastrado: '))
  arquivos.write(nomes+'\n')
arquivos.close()

arquivos = open('Dados.txt', 'r');
nome = arquivos.read()


print(f'Os nomes cadastratos são: \n{nome}')