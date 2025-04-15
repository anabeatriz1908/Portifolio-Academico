N =int(input())
sub = 1
cont = 1

if 0 < N < 13: # condiçao para validar o codigo
    while sub < N: # para fazer o fatorial (N-1), (N-2)...(1)
        cont *= (N- sub)
        sub += 1
        
# N * (N-1) * (N-2) * (N-3) * (N-N)

expressao = N * cont
print(expressao)