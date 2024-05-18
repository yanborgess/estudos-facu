matrix = []

for i in range(2):
    senha = []
    for i in range(2):
        senhas = int(input('Digite a senha a ser cadastrada => '))
        senha.append(senhas)
    matrix.append(senha)

entrada = int(input('Digite a sua senha => '))

if entrada in matrix[0] or entrada in matrix[1]:
    print('BEM VINDO!!')
else:
    print('NÃO AUTORIZADO!')
