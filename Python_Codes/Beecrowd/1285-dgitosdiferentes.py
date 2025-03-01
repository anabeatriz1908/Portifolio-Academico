while True:
    try:
        n,m = input().split(' ')
        n, m = int(n), int(m)
        
        qtd = 0
        
        for num in range(n, m+1):
            num = str(num)
            x = set(num)
            if len(num) == len(x):
                qtd += 1
                
        print(qtd)
                
        
    
    except EOFError:
        break