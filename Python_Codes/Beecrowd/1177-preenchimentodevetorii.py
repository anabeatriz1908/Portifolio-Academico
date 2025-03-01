num = int(input()) # tam do intervalo na repetição
lista = [0]*num
pos = 0

while pos < num:
    lista[pos] = pos
    pos += 1
    
lim = 0
for n in range(1000):
    if pos > num-1:
        pos = 0
    print(f'N[{lim}] = {lista[pos]}')
    pos += 1
    lim +=1