pos = 0
num = []

while pos < 10:
    num.append(int(input()))
    pos+=1

pos = 0
for n in num:
    if n == 0 or n < 0:
        print(f'X[{pos}] = 1')
    
    else:
        print(f'X[{pos}] = {num[pos]}')
    
    pos += 1