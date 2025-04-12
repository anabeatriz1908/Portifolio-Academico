A, B, C= input().split(" ")

A= float(A)
B= float(B)
C= float(C)

# RAIZ(B^2 * -4.A.C)
raiz = B**2 + (-4 *A*C)

# Importando a matemática
import math

# trabalhando com a importação da matematica
if raiz > 0:
    raiz = math.sqrt(raiz)
    
    # (-B +_ RAIZ DE termo)/2*A
    if A > 0:
        bha1 = (-(B) + raiz)/ (2*A)
        bha2 = (-(B) - raiz)/ (2*A)
        print(f'R1 = {bha1:.5f}')
        print(f'R2 = {bha2:.5f}')
    
    else:
        print('Impossivel calcular')

else:
    print('Impossivel calcular')
