casos =  int(input())
gabarito = []
for caso in range(casos):
    resposta = int(input())
    gabarito.append(resposta)

for pos in range(len(gabarito)):
    print(f'resposta {pos+1}: {gabarito[pos]}')