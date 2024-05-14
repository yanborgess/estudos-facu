#01 

def perimetro(larg,comp):
    perimetro = (larg*2)+(comp*2)
    return perimetro

#02

def media(n1,n2,n3):
    media = (n1+n2+n3)/3
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
        print('O primeiro número e o maior')
    else:
        print('O segundo número e o maior')
    return maior 