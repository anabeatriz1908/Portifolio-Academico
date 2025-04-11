a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

def quant_pares(a,b,c,d,e):
    numeros = [a,b,c,d,e]
    pares = 0
    for num in numeros:
        if num % 2 ==0:
            pares += 1
    return pares

quan_par = quant_pares(a,b,c,d,e)

print(f'{quan_par} valores pares')
