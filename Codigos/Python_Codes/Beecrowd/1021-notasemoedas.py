valor = float(input())

# contadores
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0

if 0 <= valor <= 1000000:
    while valor >= 100:
        n100 += 1
        valor -= 100
    
    while valor >= 50:
        n50 += 1
        valor -= 50
    
    while valor >= 20:
        n20 += 1
        valor -= 20
    
    while valor >= 10:
        n10 += 1
        valor -= 10
        
    while valor >= 5:
        n5 += 1
        valor -= 5
    
    while valor >= 2:
        n2 += 1
        valor -= 2
        
    # moedas

    mo100 = 0
    mo050 = 0
    mo025 = 0
    mo010 = 0
    mo005 = 0
    mo001 = 0
    
    while valor >= 1:
        mo100 += 1
        valor -= 1
        valor = round(valor, 2)
        
    while valor >= 0.50:
        mo050 += 1
        valor -= 0.50
        valor = round(valor, 2)
        
    while valor >= 0.25:
        mo025 += 1
        valor -= 0.25
        valor = round(valor, 2)
        
    while valor >= 0.10:
        mo010 += 1
        valor -= 0.1
        valor = round(valor, 2)
        
    while valor >= 0.05:
        mo005 += 1
        valor -= 0.05
        valor = round(valor, 2)
        
    while valor >= 0.01:
        mo001 += 1
        valor -= 0.01
        valor = round(valor, 2)
    
    print('NOTAS:')
    print(n100,'nota(s) de R$ 100.00')
    print(n50,'nota(s) de R$ 50.00')
    print(n20,'nota(s) de R$ 20.00')
    print(n10,'nota(s) de R$ 10.00')
    print(n5,'nota(s) de R$ 5.00')
    print(n2,'nota(s) de R$ 2.00')
    print('MOEDAS:')
    print(mo100,'moeda(s) de R$ 1.00')
    print(mo050,'moeda(s) de R$ 0.50')
    print(mo025,'moeda(s) de R$ 0.25')
    print(mo010,'moeda(s) de R$ 0.10')
    print(mo005,'moeda(s) de R$ 0.05')
    print(mo001,'moeda(s) de R$ 0.01')
