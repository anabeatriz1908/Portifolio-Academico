# lanchonete

# codigo1 = cachorro quente = 4
#codigo2 = x-salada = 4.5
#codigo3 = x-bacon = 5
#codigo4 = torrada simples = 2
#codigo5 = refrigerante = 1

x, y = input().split(' ')

x,y = int(x), int(y)

if x == 1:
    conta = 4 * y

elif x == 2:
    conta = 4.5 * y
    
elif x == 3:
    conta = 5 * y
    
elif x == 4:
    conta = 2 * y
    
elif x == 5:
    conta = 1.5 * y
    
print(f'Total: R$ {conta:.2f}')
    
