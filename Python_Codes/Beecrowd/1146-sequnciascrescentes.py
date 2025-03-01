while True:
    x = int(input())
    if x == 0: break
    else:
        for num in range(1, x+1):
            if num == x:
                print(num, end = '')
            else:
                print(num, end = ' ')
        print()