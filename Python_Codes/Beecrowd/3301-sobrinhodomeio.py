while True:
    try:
        idades = []
        h,z,l = map(int, input().split(' '))
        idades = [['huguinho', h], ['zezinho', z], ['luisinho', l]]
        idades.sort(key=lambda item:item[1])
        print(idades[1][0])
        
    except EOFError:
        break