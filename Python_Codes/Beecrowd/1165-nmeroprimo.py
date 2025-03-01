casos = int(input())

for caso in range(casos):
    num = int(input())
    div = 1
    cont = 0
    while div <= num:
        if num % div == 0:
            cont += 1
        div += 1
        
    if cont == 2:
        print(num,'eh primo')
        
    else:
        print(num,'nao eh primo')