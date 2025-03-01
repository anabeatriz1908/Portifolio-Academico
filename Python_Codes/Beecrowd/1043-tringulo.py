a,b,c = input().split(' ')
a,b,c = float(a), float(b), float(c)

if a < (c+b) and c < (a+b) and b < (c+a):
    print(f'Perimetro = {a+b+c}')

else: print(f'Area = {(((a+b)*c)/2)}')