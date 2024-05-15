from funcoes import velocidademedia

kmfi = int(input('Digite o km final: '))
kmin = int(input('Digite o km inicial: '))
hrfi = int(input('Digite a hora final: '))
hrin = int(input('Digite a hora inicial: '))

result = velocidademedia(kmfi,kmin,hrfi,hrin)

print(f'A velocidade media  é igual a: {result:.2f} km')