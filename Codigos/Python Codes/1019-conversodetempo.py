n = int(input())
h = 0
m = 0
s = 0

while n >= 3600:
    h += 1
    n -=3600

while n >= 60:
    m += 1
    n -= 60

s = n # é oq sobrou dos segundos iniciais, a variavel s (segundos)
# passa a receber o valor de n 

print(f'{h}:{m}:{s}')