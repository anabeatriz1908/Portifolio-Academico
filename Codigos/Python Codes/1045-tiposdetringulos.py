a,b,c = input().split(' ')
a,b,c = float(a), float(b), float(c)
# a é o maior dos lados
lista = [a,b,c]
lista = sorted(lista, reverse =  True)

if lista[0] >= (lista[1]+lista[2]):
    print('NAO FORMA TRIANGULO')
elif lista[0]**2 == (lista[1]**2 + lista[2]**2):
    print('TRIANGULO RETANGULO')
elif lista[0]**2 > (lista[1]**2 + lista[2]**2):
    print('TRIANGULO OBTUSANGULO')
elif lista[0]**2 < (lista[1]**2 + lista[2]**2):
    print('TRIANGULO ACUTANGULO')

if lista[0] == lista[1] == lista[2]:
    print('TRIANGULO EQUILATERO')
elif lista[0] == lista[1] or lista[1] == lista[2] or lista[0] ==lista[2]:
    print('TRIANGULO ISOSCELES')