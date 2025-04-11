s = 1
exp = 1

for num in range(3, 39+1, 2):
    s += num/(2**exp)
    exp += 1
print(f'{s:.2f}')