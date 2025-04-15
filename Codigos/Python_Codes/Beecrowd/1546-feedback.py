casos = int(input())

for caso in range(casos):
    qtd_feed =  int(input())
    for f in range(qtd_feed):
        feed =  int(input())
        if feed == 1:
            print('Rolien')
        elif feed == 2:
            print('Naej')
        elif feed == 3:
            print('Elehcim')
        else:
            print('Odranoel')