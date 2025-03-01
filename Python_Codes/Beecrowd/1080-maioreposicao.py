lista = [0]*100
pos = 0
# PREENCHENDO A LISTA
while pos < 100:
    lista[pos] = int(input())
    pos += 1

# VERIFICANDO O MAIOR
pos = 0
m = 0
while pos < 100:
    if lista[pos] > m:
        m = lista[pos]
        posicao = pos + 1 # pq lista comeca do zero
        
    pos += 1

# EXIBINDO
print(m)
print(posicao)