
for i in range(1,4):
    nome_pessoa = input(f"Digite o nome da {i}ª pessoa: ")
    telefone_pessoa = input(f"Digite o telefone da {i}ª pessoa: ")
    nome_arquivo = input(f"Digite o nome do arquivo a ser criado para a {i}ª pessoa: ")
    arquivo = open(nome_arquivo, 'w') 
    arquivo.write(f'{nome_pessoa}\n')
    arquivo.write(f'{telefone_pessoa}\n')

nome_arquivo = input("Digite o nome do arquivo a ser lido: ")
arquivo = open(nome_arquivo, 'r')
conteudo = arquivo.readlines()
if len(conteudo) >= 2:
                nome_pessoa = conteudo[0]
                telefone_pessoa = conteudo[1]
                print(f"Nome: {nome_pessoa}")
                print(f"Telefone: {telefone_pessoa}")

    



