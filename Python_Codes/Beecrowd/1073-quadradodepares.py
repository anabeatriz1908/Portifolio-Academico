n = int(input())
q = 2
if 5 < n < 2000:
    while q <= n:
        print(f'{q}^{2} = {q**2}')
        q += 2