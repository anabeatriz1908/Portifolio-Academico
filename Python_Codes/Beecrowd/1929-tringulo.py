def forma_triangulo(a,b,c,d):
    if a + b > c and a + c > b and b + c > a:
        return 'S'
    elif a + b > d and a + d > b and b + d > a:
        return 'S'
    elif a + c > d and a + d > c and c + d > a:
        return 'S'
    elif c + b > d and c + d > b and b + d > c:
        return 'S'
    else:
        return 'N'

a,b,c,d = map(int, input().split(' '))
print(forma_triangulo(a,b,c,d))