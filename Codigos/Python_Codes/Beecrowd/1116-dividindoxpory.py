casos = int(input())

for caso in range(casos):
    x, y = map(int, input().split(' '))
    if y == 0: print('divisao impossivel')
    else:
        print(f'{(x/y):.1f}')