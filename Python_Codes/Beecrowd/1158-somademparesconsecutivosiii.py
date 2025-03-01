casos = int(input())

for caso in range(casos):
    x,y = map(int, input().split(' '))
    soma = 0
    while y >= 1:
        if x % 2 != 0:
            soma += x
            y -= 1
        x += 1
        
    print(soma)