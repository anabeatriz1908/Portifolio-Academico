a,b,c = input().split(' ')

a,b,c = int(a), int(b), int(c)

if a > b:
    if a > c:
        print(a,'eh o maior')
        
    else:
        print(c,'eh o maior')

else:
    if b > c:
        print(b,'eh o maior')
    
    else:
        print(c,'eh o maior')
