i = 0; j = 1

while i <= 2:
    cont = 0
    while cont < 3:
        if round(i,1) == 0 or round(i, 1) == 1.0 or round(i,1) == 2.0:
            print(f'I={i:.0f} J={j:.0f}')
        else:
            print(f'I={i:.1f} J={j:.1f}')
        cont += 1
        j += 1
    # começo de outro loop de cont
    j -= 3
    i += 0.2
    j += 0.2