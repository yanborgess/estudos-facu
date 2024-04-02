contador_jogador1 = 0
contador_jogador2 = 0

while True:

    print("=-=-=-=-=-= JOKEN PO =-=-=-=-=-=")

    print('''\n   ESCOLHA SUA OPÇÃO:
      [1] PEDRA
      [2] TESOURA
      [3] PAPEL ''')
    print('\n---------------------------------')

    jogador1= int(input('\nJOGADOR 1 QUAL SUA OPÇÃO? '))
    jogador2 = int(input('JOGADOR 2 QUAL SUA OPÇÃO? '))

    if jogador1 ==1:
        if jogador2 ==  1:
            print('EMPATE!!')
        elif jogador2 == 2:
            print('JOGADOR 1 VENCEU!!')
            contador_jogador1 +=1
        elif jogador2 == 3:
            print('JOGADOR 2 GANHOU!!')
            contador_jogador2+=1

    if jogador1 == 2:
        if jogador2 == 2:
            print('EMPATE!!')
        elif jogador2 == 1:
            print('JOGADOR 2 VENCEU!!')
            contador_jogador2+=1
        elif jogador2 == 3:
            print('JOGADOR 1 VENCEU!!')
            contador_jogador1+=1

    if jogador1 == 3:
        if jogador2 ==3:
            print('EMPATE!!')
        elif jogador2 == 1: 
            print('JOGADOR 1 VENCEU!!')
            contador_jogador1+=1
        elif jogador2 == 2:
            print('JOGADOR 2 GANHOU!!!')
            contador_jogador2+=1
        
    print(f'\nPONTUAÇAO DOS JOGADOR 1: {contador_jogador1}')
    print(f'PONTUAÇAO JOGADOR 2: {contador_jogador2}')

    if contador_jogador1  == 2:
        print('JOGADOR 1 VENCEU!!')
        break
    elif contador_jogador2 == 2:
        print('JOGADOR 2 VENCEU!!')
        break






















