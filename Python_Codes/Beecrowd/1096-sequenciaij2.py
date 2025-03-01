i = 1; j = 7
cont = 0
while i <= 9:
    while cont < 3:
        print(f'I={i} J={j}')
        j -= 1
        cont+= 1
    i += 2
    cont = 0
    j = 7