casos = int(input())
dentro = 0
fora = 0

for caso in range(casos):
    num = int(input())
    if num >= 10 and num <=20: dentro += 1
    else: fora +=1

print(dentro,'in')
print(fora,'out')