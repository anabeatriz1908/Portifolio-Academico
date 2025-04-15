while True:
    x = int(input())
    if x == 0:
        break
    
    else:
        soma = 0
        cont = 0
        
        # loop para somar os 5 pares 
        while cont < 5:
            if x % 2 == 0:
                soma += x; x += 2; cont += 1
            else:
                x += 1
        print(soma)