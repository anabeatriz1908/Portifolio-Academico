pos = 0
N = []

while pos < 20:
    N.append(int(input()))
    pos += 1

pos = 0
pos_2 = 19

while pos < 10: # pos_total = 19. 19 // 2 = 9
    temp = N[pos]
    N[pos] = N[pos_2]
    N[pos_2] = temp
    pos +=1
    pos_2 -= 1

pos = 0
for num in N:
    print(f'N[{pos}] = {N[pos]}')
    pos += 1