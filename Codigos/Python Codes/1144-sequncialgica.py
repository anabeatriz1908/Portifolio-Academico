n = int(input())
num = 1
for _ in range(n):
    print(f'{num} {num**2} {num**3}')
    print(f'{num} {num**2 + 1} {num**3 + 1}')
    num += 1