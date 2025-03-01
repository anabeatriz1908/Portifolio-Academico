condicao = True
a = 0
g = 0
d = 0

while condicao:
    opcao = int(input())
    if opcao == 1:
        a += 1
    elif opcao == 2:
        g += 1
    elif opcao == 3:
        d += 1
    elif opcao == 4:
        condicao = not condicao

print('MUITO OBRIGADO')
print('Alcool:',a)
print('Gasolina:',g)
print('Diesel:',d)