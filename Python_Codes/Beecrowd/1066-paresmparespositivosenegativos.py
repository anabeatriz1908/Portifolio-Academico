pares = 0
impares = 0
positivos = 0
negativos = 0

for num in range(5):
    num = int(input())
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(pares,'valor(es) par(es)')
print(impares,'valor(es) impar(es)')
print(positivos,'valor(es) positivo(s)')
print(negativos,'valor(es) negativo(s)')