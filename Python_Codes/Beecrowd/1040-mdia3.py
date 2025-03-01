a,b,c,d = input().split(" ")

a= float(a)
b= float(b)
c= float(c)
d= float(d)

# calculo da media
media = ((a*2) + (b*3) + (c*4) + (d*1))/10
print(f'Media: {media:.1f}')

# aprovado
if media >=7.0:
    print('Aluno aprovado.')

# reprovado
if media < 5.0:
    print('Aluno reprovado.')

# em exame
if 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    print('Nota do exame:', nota_exame)
    
    # recalculando
    nota= (media + nota_exame)/2
    
    if nota >= 5.0:
        print('Aluno aprovado.')
        
    else:
        print('Aluno reprovado')
        
    print('Media final:', nota)
