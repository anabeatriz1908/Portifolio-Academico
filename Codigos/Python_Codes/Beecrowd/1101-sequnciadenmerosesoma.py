while True:
    try:
        x,y = map(int, input().split(' '))
        if x <= 0 or y <= 0: break
        
        #concatenação, aqui se x for maior, a ordem dos elementos é trocada
        # ex: [5..2] virá [2..5]
        if x > y: x,y = y,x
        
        # criando uma variavel para receber a soma dos numeros 
        soma = 0 # a cada iteração ela será definida como zero
        
        # percorrendo o intervalo [x..y]
        for num in range(x,y+1):
            soma += num # soma recebe o num
            print(num, end = ' ') # a exibição fará que os numeros fiquem na mesma linha
                                    # separados por um espaço ' '
        
        print(f'Sum={soma}')  # ainda na mesma linha, a variavel soma exibida
    except: EOFError 