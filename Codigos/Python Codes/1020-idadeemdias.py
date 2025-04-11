idade = int(input())
ano = 0
mes = 0
dia = 0

while idade>=365:
    ano +=1
    idade -= 365
    
    
while idade >= 30:
    mes += 1
    idade -=30

dia = idade

print(ano,'ano(s)')
print(mes,"mes(es)")
print(dia,'dia(s)')
    