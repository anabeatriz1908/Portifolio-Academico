a,b,c = input().split(' ')
a,b,c = int(a), int(b), int(c)

lista = [a,b,c]
nova_lista = lista[:]

lista.sort()
for num in lista:
    print(num)
    
print()
for n in nova_lista:
    print(n)