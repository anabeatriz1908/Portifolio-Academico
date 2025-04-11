lista = []
media = 0
for n in range(6):
    num = float(input())
    if num > 0:
        lista.append(num)
        media += num

# valores positivos
tam = len(lista)
print(f'{tam} valores positivos')

# medias dos valores positivos
media = media/tam
print(f'{media:.1f}')