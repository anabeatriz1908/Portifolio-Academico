# Inter Grêmio. Numeros de Vitorias
inter = 0
gremio = 0
empate = 0

while True:
    i, g = map(int, input().split(' '))
    if i > g: inter += 1
    elif g > i: gremio += 1
    else: empate += 1
    print('Novo grenal (1-sim 2-nao)')
    grenal = int(input())
    if grenal == 2: break

print(f'{inter+gremio+empate} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')

if inter>gremio:
    print('Inter venceu mais')
elif inter == gremio:
    print('Nao houve vencedor')
else:
    print('Gremio venceu mais')