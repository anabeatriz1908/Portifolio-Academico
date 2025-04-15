while True:
    try:
        num = int(input())
        if num <= 0: 
            print('vai ter copa!')
        else:
            print(f'vai ter duas!')
    except EOFError:
        break