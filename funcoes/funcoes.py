#01 

def perimetro(larg,comp):
    perimetro = (larg*2)+(comp*2)
    return perimetro

#02

def media(n1,n2,n3):
    media = (n1+n2+n3)/3
    if media < 7:
        print('REPROVADO')
    else:
        print('APROVADO!!')
    return media

#03

def velocidademedia(kmin,kmfi,hrin,hrfi): 
    return (kmfi - kmin)/(hrfi-hrin)
    
#04

def preco(prod,valor):
    valores = valor * prod
    return valores

#05

def checapositivo(pos):
    if pos >0:
        print ('ele e positivo')
    else:
        print('ele e negativo')
    
    return pos

#06 

def maior (n1,n2):
    if n1 >n2:
        print('O primeiro número é o maior')
    else:
        print('O segundo número é o maior')
    return maior 

#07


#08
def soma(n1,n2):
    soma = n1 + n2
    print(f'a soma entre {n1} e {n2}, é igual a: {soma}')
    return soma

def subtracao(n1,n2):
    sub = n1 - n2 
    print(f'A subtração entre {n1} e {n2} e igual a: {sub}')
    return sub

def mult(n1,n2):
    mult = n1 * n2
    print(f'A multiplicaçao entre {n1} e {n2} e igual a :',mult)
    return mult

def div(n1,n2):
    div = n1 / n2 
    print(f'A dvisao entre {n1} e {n2} e igual a: ', div)
    return div 

#09
def segundos_(horas, minutos, segundos):
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos

#10

def media2(n1,n2):
    media = (n1+n2) /2
    print('A media entre eles são:',media)
    return media 

def diferenca(n1,n2):
    if n1 < n2:
        maior1= n2 - n1 
        print('A diferença entre eles são:',maior1)
    else:
        maior2 =  n1 - n2 
        print('A diferença entre eles são:',maior2)

def produto(n1,n2):
    produtos =  n1*n2 
    print('O produto entre os números são:',produtos)
    return produtos

def div2(n1,n2):
    div = n1 / n2 
    print('A divisão entre eles é igual á:',div)
    return div

