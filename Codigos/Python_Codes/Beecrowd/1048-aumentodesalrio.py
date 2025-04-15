s = float(input())

if s <=400 and s >= 0:
    p = 0.15
    novo_s = s + (s*p)
    reajuste = novo_s - s
    
elif s > 400.00 and s <= 800:
    p = 0.12
    novo_s = s + (s*p)
    reajuste = novo_s - s
    
elif s > 800.0 and s <= 1200:
    p = 0.10
    novo_s = s + (s*p)
    reajuste = novo_s - s
    
elif s > 1200.00 and s <= 2000:
    p = 0.07
    novo_s = s + (s*p)
    reajuste = novo_s - s
    
else:
    p = 0.04
    novo_s = s + (s*p)
    reajuste = novo_s - s

# exibindo
print(f'Novo salario: {novo_s:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {p*100:.0f} %')