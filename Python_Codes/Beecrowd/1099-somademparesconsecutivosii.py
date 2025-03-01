casos = int(input())

for caso in range(casos):
    soma = 0
    x, y = map(int, input().split(' '))
    if x > y: x,y = y,x 
    
    for num in range(x + 1,y):
        if num % 2 != 0:
            soma += num
    
    print(soma)