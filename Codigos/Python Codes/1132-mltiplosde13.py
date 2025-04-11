a = int(input())
b = int(input())
soma_13 = 0

if a > b:
    a,b = b,a

while a <= b:
    if a % 13 != 0: soma_13 += a
    a += 1

print(soma_13)