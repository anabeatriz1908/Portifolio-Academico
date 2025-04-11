inicio,fim = map(int, input().split(' '))

horas = 0
if inicio > fim or inicio == fim:
    while inicio < 24:
        horas += 1
        inicio += 1
    
    while fim > 0:
        horas += 1
        fim -= 1
elif inicio < fim:
    horas = fim - inicio
    
print(F'O JOGO DUROU {horas} HORA(S)')
