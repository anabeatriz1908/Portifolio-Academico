'''
Crie uma classe chamada Retângulo que represente um retângulo. 
A classe deve possuir atributos para largura e altura, além de métodos para:

Calcular a área do retângulo.
Calcular o perímetro do retângulo.
Redimensionar o retângulo, alterando sua largura e altura.
Exibir as propriedades (largura e altura) do retângulo.

Implemente a classe e teste suas funcionalidades instanciando objetos e chamando seus métodos.
'''
#%%
class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    
    def calcular_area(self):
        print(f"{self.altura*self.largura} cm²")

    def calcular_perimetro(self):
        print(f"{self.altura*2 + self.largura*2} cm")
    
    def redimensiona_retangulo(self, nova_altura, nova_largura):
        self.altura = nova_altura
        self.largura = nova_largura
    
    def exibi_informacoes(self):
        print(F"Informações sobre o retângulo:")
        print(f"Altura: {self.altura} cm")
        print(f"Largura: {self.largura} cm")

#%%
#PROGRAMA PRINCIPAL

#Criando o objeto da classe Retangulo
retangulo01 = Retangulo(3,2)

#Calculando a area do retangulo01
retangulo01.calcular_area()

#Calculando o perimetro do retangulo01
retangulo01.calcular_perimetro()

#Exibindo as informações do retangulo01
retangulo01.exibi_informacoes()

#Mudando a altura e largura do retangulo01
retangulo01.redimensiona_retangulo(5,4)

#Exbindo as informações do retangulo01 após modificar a altura
retangulo01.exibi_informacoes()




# %%
