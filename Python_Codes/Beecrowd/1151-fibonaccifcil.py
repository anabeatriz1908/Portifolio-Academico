# função que cria a sequencia com base no tamanho oferecido pelo usuario
def limita_sequencia(tam):
    # preenchendo a lista
    fibo = [0, 1] # posições iniciais de fibonacci
    pos = 0
    while pos < tam - 2:
        fibo.append(fibo[pos] + fibo[pos + 1])
        pos += 1
    return fibo

def exibe_sequencia(fibo, tam):
    for i in range(tam):
        if i == tam - 1:
            print(fibo[i], end = '')
        else:
            print(fibo[i], end = ' ')
    print()

num = int(input())
seq_num = limita_sequencia(num)
exibe_sequencia(seq_num, num)