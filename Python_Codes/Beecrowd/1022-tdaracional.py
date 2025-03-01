# importando a biblioteca de frações:
from fractions import Fraction

# qtd de casos
num_casos = int(input())

# percorrendo a qtd de casos
for caso in range(num_casos):
    n1, s1, d1, sinal, n2, s2, d2 = input().split(' ')
    n1,n2,d1,d2 = int(n1), int(n2), int(d1), int(d2)
#   1     /   2     +     3   /   4
    # transformando os valores em fração
    frac1 = Fraction(int(n1), int(d1))
    frac2 = Fraction(int(n2), int(d2))

    if sinal == '+': #   Soma: (N1*D2 + N2*D1) / (D1*D2)
        f1 = (n1*d2 + n2*d1)
        f2 = (d1*d2)
        resul = frac1 + frac2
        
    elif sinal == '-': #   Subtração: (N1*D2 - N2*D1) / (D1*D2)
        f1 = (n1*d2 - n2*d1)
        f2 = (d1*d2)
        resul = frac1 - frac2
        
    elif sinal == '*': #   Multiplicação: (N1*N2) / (D1*D2)
        f1 = (n1*n2)
        f2 = (d1*d2) 
        resul = frac1 * frac2
    else: #   Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)
        f1 = (n1*d2)
        f2 = (n2*d1)
        resul = frac1 / frac2
    
    if f1 % f2 == 0:
        print(f'{f1}/{f2} = {resul}/1')
    else:
        print(f'{f1}/{f2} = {resul}')