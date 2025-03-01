x,y = map(int, input().split(' '))
num = 1
while num <= y:
    for coluna in range(x):
        if coluna == x - 1:
            print(num, end = '')
        else:
            print(num, end = ' ')
        num += 1
    print()