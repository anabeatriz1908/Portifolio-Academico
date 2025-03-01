n = int(input())

# caso n for maior que 50
while n > 50:
    n = int(input())

# para indicar o indice
i = 0

for num in range(10):
    print(f'N[{i}] = {n}')
    i += 1
    n *=2
