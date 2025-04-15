escolha, num1, num2, roubo, acusa = map(int, input().split(' '))

# somando os numeros escolhidos para definir se irá ser par ou não
soma = num1 + num2

# definindo o resultado
if soma % 2 == 0: resultado = 1 # par
else: resultado = 0 # impar

# definindo o ganhador com base no resultado
# o jogador 1 sempre escolhe se é par ou impar. se o resultado for o mesmo da escolha inicial, ele ganha
if escolha == 1 and resultado == 1: ganhador = 1 
elif escolha == 0 and resultado == 0: ganhador = 1
else: ganhador = 2

# aqui indica se o jogador 1 vai escolher ou não roubar
if ganhador == 2 and roubo == 1: 
    ganhador = 1


if ganhador == 2:
    if roubo == 0:
        if acusa == 0: ganhador = 2
        else: ganhador = 1
    else:
        if acusa == 1: ganhador = 2
        else: ganhador = 1
else:
    if roubo == 0:
        if acusa == 0: ganhador = 1
        else: ganhador = 1
    else:
        if acusa == 1: ganhador = 2
        else: ganhador = 1
            
print(f'Jogador {ganhador} ganha!')