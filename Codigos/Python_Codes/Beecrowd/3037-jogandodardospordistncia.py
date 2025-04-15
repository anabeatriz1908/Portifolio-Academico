# CASOS DE TESTE
num_casos = int(input())

# percorrendo os casos de teste
for caso in range(num_casos):
    pontos_joao = 0
    pontos_maria = 0
    for num in range(3):#rodada do joão
        x,d = input().split(' ')
        x,d = int(x), int(d)
        pontos_joao += x*d
    for num in range(3):#rodada maria
        x,d = input().split(' ')
        x,d = int(x), int(d)
        pontos_maria += x*d
    
    if pontos_joao > pontos_maria:
        print('JOAO')
    else:
        print('MARIA')
