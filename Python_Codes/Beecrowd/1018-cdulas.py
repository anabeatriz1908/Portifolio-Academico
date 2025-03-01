valor = int(input())

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

if 0 < valor < 1000000:
    print(valor)
    while valor >= 100:
        nota100 += 1
        valor = valor - 100
    
    while valor >= 50:
        nota50 += 1
        valor = valor - 50
        
    while valor >= 20:
        nota20 += 1
        valor = valor - 20
    
    while valor >= 10:
        nota10 += 1
        valor = valor - 10
        
    while valor >= 5:
        nota5 += 1
        valor = valor - 5
        
    while valor >= 2:
        nota2 += 1
        valor = valor - 2
        
    while valor >= 1:
        nota1 += 1
        valor = valor - 1
        
    print(nota100,'nota(s) de R$ 100,00')
    print(nota50,'nota(s) de R$ 50,00')
    print(nota20,'nota(s) de R$ 20,00')
    print(nota10,'nota(s) de R$ 10,00')
    print(nota5,'nota(s) de R$ 5,00')
    print(nota2,'nota(s) de R$ 2,00')
    print(nota1,'nota(s) de R$ 1,00')

else:
    print('Informe um valor válido')