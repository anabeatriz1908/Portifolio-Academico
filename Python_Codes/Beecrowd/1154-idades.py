idade = int(input())
media = idade
cont = 1


while idade > 0:
    idade = int(input())
    if idade > 0:
        media += idade
        cont += 1
    
    
media = media/cont

print(f'{media:.2f}')