while True:
    try:
        x, y = map(int, input().split(' '))
        if x < y: print('Crescente')
        elif x == y: break
        else: print('Decrescente')
    except: EOFError