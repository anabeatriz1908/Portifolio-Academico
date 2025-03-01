casos = int(input())

for caso in range(casos):
    soma = 0
    num = int(input())
    div = 1
    while div < num:
        if num % div == 0:
            soma += div
        div += 1
    if soma == num:
        print(num,'eh perfeito')
        
    else:
        print(num,'nao eh perfeito')