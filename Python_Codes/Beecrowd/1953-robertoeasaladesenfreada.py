while True:
    try:
    # variaveis com os nomes dos cursos
        alunos = int(input())
        EPR = 0
        EHD = 0
        INTRUSOS = 0
        
        for aluno in range(alunos):
            ra, curso = input().split(' ')
            
            # validando qual ra faz parte de cada curso
            if curso == 'EPR':
                EPR += 1
            elif curso == 'EHD':
                EHD += 1
            else:
                INTRUSOS += 1
        # exibindo as mensagens
        print('EPR:',EPR)
        print('EHD:',EHD)
        print('INTRUSOS:',INTRUSOS)
    except EOFError:
        break