for i in range(1,5):
    nomes =  input(f'Digite o nome do {i}º aluno: ')
    notas = []
    for j in range(1,4):
        nota = float(input(f"Digite a {j}ª nota do {i}º aluno: "))
        notas.append(nota)
    
    nome_arquivo = input(f"Digite o nome do arquivo a ser criado para o {i}º aluno: ")

    arquivo = open(nome_arquivo, 'w')
    arquivo.write(f'{nomes}\n')
    for nota in notas:
        arquivo.write(f"{nota}\n")

nome_arquivo = input("Digite o nome do arquivo a ser lido: ")
    
arquivo = open(nome_arquivo, 'r')
conteudo = arquivo.readlines()
            
if len(conteudo) >= 4:
                nome_aluno = conteudo[0].strip()
                notas = [float(conteudo[i].strip()) for i in range(1, 4)]
                print(f"Nome: {nome_aluno}")
                for i, nota in enumerate(notas, start=1):
                    print(f"Nota {i}: {nota}")

