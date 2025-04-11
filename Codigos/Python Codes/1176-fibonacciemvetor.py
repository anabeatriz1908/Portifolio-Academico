# criando a função que vai gerar minha lista
def gera_sequencia_fibonacci():
    fibonacci = [0,1] # numeros pré-estabelecidos para a sequencia
    for i in range(60): fibonacci.append(fibonacci[i] + fibonacci[i+1])
    return fibonacci
    
# chamando a função da sequencia de fibonacci
sequencia_de_fibonacci = gera_sequencia_fibonacci()

# numero de casos que serão consultados
casos = int(input())

for _ in range(casos):
    posicao = int(input())
    print(f'Fib({posicao}) = {sequencia_de_fibonacci[posicao]}')