a,b,c,d = input().split(' ')
a,b,c,d = int(a), int(b), int(c), int(d)

if b > c:
    if d > a:
        if (c + d) > (a + b):
            if c > 0 and d > 0:
                if a % 2 == 0:
                   print('Valores aceitos')
                else:
                    print('Valores nao aceitos')
            else:
                 print('Valores nao aceitos')
        else:
            print('Valores nao aceitos')
    else:
        print('Valores nao aceitos')
else:
    print('Valores nao aceitos')
