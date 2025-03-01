casos = int(input())
lista = []
for caso in range(casos):
    ra, nota = input().split(' ')
    ra, nota = int(ra), float(nota)
    if nota >= 8:
        lista.append([ra,nota])

# percorrendo a lista de notas
maior = 0 # maior vai receber a nota do aluno com a maior nota
melhor_aluno = 0
for l in lista:
    if l[1] > maior:
        maior = l[1]
        melhor_aluno = l[0]
        
# exibindo o ra da maior nota
if maior == 0: print('Minimum note not reached')
else: print(melhor_aluno)