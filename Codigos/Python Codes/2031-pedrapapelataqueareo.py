casos = int(input())

for caso in range(casos):
    ganhador = 0
    jogador1 = input()
    jogador2 = input() # ataque, pedra ou papel
    
    # 0 --> Sem ganhador
    # 1 --> jogador1
    # 2 --> jogador2
    # 3 --> Ambos venceram
    # 4 --> Anililação mutua

    if jogador1 == 'pedra':
        if jogador2 == 'pedra': ganhador = 0
        elif jogador2 == 'papel': ganhador = 1
        else: ganhador = 2
    
    elif jogador1 == 'papel':
        if jogador2 == 'pedra': ganhador = 2
        elif jogador2 == 'papel': ganhador = 3
        else: ganhador = 2
    
    elif jogador1 == 'ataque':
        if jogador2 == 'pedra': ganhador = 1
        elif jogador2 == 'papel': ganhador = 1
        else: ganhador = 4
        
    # exibição
    if ganhador == 3: print('Ambos venceram')
    elif ganhador == 0: print('Sem ganhador')
    elif ganhador == 4: print('Aniquilacao mutua')
    else: print(f'Jogador {ganhador} venceu')