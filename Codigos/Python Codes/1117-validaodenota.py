media = 0
pos = 0

while pos < 2:
    nota = float(input())
    if nota <=10 and nota >= 0:
        media += nota
        pos += 1
        
    else:
        print('nota invalida')

print(f'media = {(media/2):.2f}')