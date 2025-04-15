P = 0
A = []

while P < 100:
    A.append(float(input()))
    P +=1

# pos com valor <= 10 e o valor em cada uma das posições

pos = 0
for num in A:
    if num <=10:
        print(f'A[{pos}] = {A[pos]}')
    pos+= 1