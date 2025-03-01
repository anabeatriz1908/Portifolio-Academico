colunas = int(input())

# multiplos de 4 ---> PUM
num = 0

for _ in range(colunas):
    lista = [num+1, num +2, num +3, num+4]
    num = num + 4
    for pos in range(4):
        if lista[pos] % 4 != 0:
            print(lista[pos], end =' ')
        else:
            print('PUM')