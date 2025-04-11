"""
Sistema Bancário com Transações Pix - Programação Orientada a Objetos (POO)

Este código simula um sistema bancário simplificado com suporte a transferências via Pix entre clientes.
Ele foi desenvolvido com base em princípios da Programação Orientada a Objetos (POO), utilizando classes,
encapsulamento, métodos e interação entre objetos.

Classes principais:

1. Cliente:
   Representa uma pessoa no sistema bancário.
   Atributos:
       - nome: Nome do cliente.
       - cpf: Cadastro de Pessoa Física (com formatação).
       - saldo: Saldo disponível na conta.
       - extrato: Lista de transações Pix realizadas ou recebidas.
   Métodos:
       - get_saldo(): Retorna o saldo atual.
       - get_extrato(): Retorna a lista de transações (extrato).
       - get_cpf(): Retorna o CPF com parte dos dígitos ocultos.
       - depositar(valor): Adiciona saldo.
       - retirar(valor): Deduz saldo.
       - realizar_pix(valor, destinatario): Cria uma transação Pix e a executa.
       - registrar_transacao(transacao): Adiciona a transação ao extrato do cliente.

2. Pix:
   Representa uma transação entre dois clientes.
   Atributos:
       - remetente: Cliente que envia o valor.
       - destinatario: Cliente que recebe o valor.
       - valor: Valor da transação.
   Métodos:
       - executar(): Realiza a transferência se o remetente tiver saldo suficiente.
         Atualiza os saldos e registra a transação nos extratos de ambos os clientes.
       - exibir_informacoes(): Exibe informações da transação com CPF parcialmente oculto.

Testes no programa principal:
   - Criação de dois clientes com saldo inicial.
   - Realização de uma transferência via Pix.
   - Verificação dos saldos antes e depois.
   - Impressão do extrato das transações com segurança de dados (CPF oculto).
   - Teste de tentativa de transferência com saldo insuficiente (não autorizada).

Este código demonstra:
   - Encapsulamento de lógica e dados.
   - Interação entre objetos.
   - Princípios de reutilização e legibilidade.
   - Segurança e privacidade em dados simulados (como CPF).

Autor(a): Ana
Disciplina: Programação Orientada a Objetos
Objetivo: Atividade preparatória com peso de até 5% da média final.
"""


# %%
class Cliente:
    def __init__(self, nome:str, cpf:str, saldo:float):
        self.nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__extrato = []

     # RETORNANDO O SALDO
    def get_saldo(self):
        return self.__saldo
        
    # RETORNANDO O EXTRATO
    def get_extrato(self):
        return self.__extrato
        
    # CPF_OCULTO
    def get_cpf(self):
        cpf_oculto = ''
        for i, char in enumerate(self.__cpf):
            if i in [4,5,6,8,9,10]: # o == não é necessário aqui
                cpf_oculto += 'X'
            else:
                cpf_oculto += self.__cpf[i]
    
        return cpf_oculto

    def depositar(self, valor):
        self.__saldo += valor # ganhou pix
        
    def retirar(self, valor):
        self.__saldo -= valor # valor saindo da conta

    def realizar_pix(self, valor, destinatario):
        transacao_pix = Pix(self, destinatario, valor)
        transacao_pix.executar()
        self.registrar_transacao(transacao_pix) 

    def registrar_transacao(self, transacao):
        self.__extrato.append(transacao)
        return self.__extrato


class Pix:
    def __init__(self, remetente: Cliente, destinatario: Cliente, valor: float):
        self.__remetente = remetente
        self.__destinatario = destinatario
        self.__valor = valor
    
    def executar(self):
        if self.__remetente.get_saldo() >= self.__valor: 
            self.__remetente.retirar(self.__valor) 
            self.__destinatario.depositar(self.__valor)
        
        else:
            print('Saldo Insuficiente')

    def exibir_informacoes(self):
        print(f'Remetente: {self.__remetente.get_cpf()}')
        print(f'Destinatário: {self.__destinatario.get_cpf()}')
        print(f'Valor: R$ {self.__valor}')


# Programa principal
cliente1 = Cliente("Maria", "123.456.789-00", 1000.0)
cliente2 = Cliente("João", "987.654.321-00", 500.0)

print(
    f"Saldo do cliente {cliente1.nome}: R${cliente1.get_saldo()}"
)  # Saldo do cliente Maria: R$1000.0

print(
    f"Saldo do cliente {cliente2.nome}: R${cliente2.get_saldo()}"
)  # Saldo do cliente João: R$500.0


cliente1.realizar_pix(200.0, cliente2)

print(
    f"Saldo do cliente {cliente1.nome}: R${cliente1.get_saldo()}"
)  # Saldo do cliente Maria: R$800.0

print(
    f"Saldo do cliente {cliente2.nome}: R${cliente2.get_saldo()}"
)  # Saldo do cliente João: R$700.0

extrato_c1 = cliente1.get_extrato()
for pix in extrato_c1:
    pix.exibir_informacoes()
# Remetente: 123.xxx.xxx-00
# Destinatário: 987.xxx.xxx-00
# Valor: R$200.0

extrato_c2 = cliente2.get_extrato()
for pix in extrato_c2:
    pix.exibir_informacoes()
# Remetente: 123.xxx.xxx-00
# Destinatário: 987.xxx.xxx-00
# Valor: R$200.0

cliente2.realizar_pix(9000.0, cliente1)
# Saldo insuficiente para realizar a transferência.


# %%
