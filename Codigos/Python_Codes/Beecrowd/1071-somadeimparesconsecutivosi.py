x = int(input())
y = int(input())
soma = 0

# entre 6 e 5.
if x > y:
    x -= 1
    while x > y:
        if x % 2 != 0:
            soma += x
        
        x -= 1
    print(soma)
    
else:
    # x < y
    # 4   6
    while y > x:
        if y % 2 != 0:
            soma += y
    
        y -= 1

    print(soma)