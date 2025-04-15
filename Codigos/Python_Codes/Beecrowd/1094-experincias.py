casos = int(input())
coelhos = 0
ratos = 0
sapos = 0
total = 0

for caso in range(casos):
    num, especie = input().split(' ')
    num = int(num)
    total += num
    if especie == 'S': sapos += num
    elif especie == 'C': coelhos += num
    else: ratos += num

porcen_1 = 100/total

print(F'Total: {total} cobaias')
print(F'Total de coelhos: {coelhos}')
print(F'Total de ratos: {ratos}')
print(F'Total de sapos: {sapos}')
print(F'Percentual de coelhos: {(coelhos*porcen_1):.2f} %')
print(F'Percentual de ratos: {(ratos*porcen_1):.2f} %')
print(F'Percentual de sapos: {(sapos*porcen_1):.2f} %')