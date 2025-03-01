def exibe(paises):
    for pais in paises:
        print(*pais)

def coleta(qtd_paises):
    paises = []
    for i in range(qtd_paises):
        n, o, p, b = input().split()
        o, p, b = int(o), int(p), int(b)
        paises.append([n, o, p, b])
    return paises

qtd_paises = int(input())
paises = coleta(qtd_paises)

# Ordenando pelos nomes.
paises.sort(key=lambda item: item[0])

# Ordenando pelas medalhas de bronze.
paises.sort(key=lambda item: item[3], reverse=True)

# Ordenando pelas medalhas de prata.
paises.sort(key=lambda item: item[2], reverse=True)

# Ordenando pelas medalhas de ouro.
paises.sort(key=lambda item: item[1], reverse=True)

exibe(paises)