from funcoes import preco

valor = float(input('Digite o valor do produto: '))
prod =  int(input('Digite a quantidade de produtos: '))

result = preco(valor, prod)
print('O valor da compra é igual a: ',result)