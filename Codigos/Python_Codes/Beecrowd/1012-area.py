A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)
pi= 3.14159

area_a= (A*C)/2
area_b= pi*C**2
area_c= ((A+B)*C)/2
area_d= B**2
area_e= A*B


print(f'TRIANGULO: {area_a:.3f}')
print(f'CIRCULO: {area_b:.3f}')
print(f'TRAPEZIO: {area_c:.3f}')
print(f'QUADRADO: {area_d:.3f}')
print(f'RETANGULO: {area_e:.3f}')
