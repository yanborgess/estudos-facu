from funcoes import segundos_

horas = int(input('Digite as horas: '))
minutos =  int(input('Digite os minutos: '))
segundos = int ( input('Digite os segundos: '))

result = segundos_(horas,minutos,segundos)

print(f'O resultado é igual a: {result:.2f}')


