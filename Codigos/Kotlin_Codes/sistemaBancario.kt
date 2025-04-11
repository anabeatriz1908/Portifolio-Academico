/*
Sistema Bancário: Crie um sistema de contas bancárias em Kotlin, utilizando os
conceitos de OO vistos em aula, seguindo as diretrizes:
• Crie a classe ContaBancaria com os seguintes atributos: nome_titular e saldo_conta. A
classe também possui os métodos depositar(valor) e sacar(valor).
• Crie a subclasse ContaCorrente que contém o atributo taxaoperacao. Toda vez que o
cliente saca dinheiro da ContaCorrente é cobrada uma taxa de R$5,00.
• Crie a subclasse ContaPoupanca que contém o atributo rendimento. Toda vez que o
cliente deposita dinheiro na Conta Poupança, o dinheiro rende 2% a mais em relação a
quantia que foi depositado.
• Implemente o método exibirSaldo() na classe ContaBancaria e em suas respectivas
subclasses.
• Crie um cliente que possua uma ContaCorrente e faça a simulação do funcionamento
dessa subclasse.
• Crie um cliente que possua ContaPoupanca e faca a simulação do funcionamento dessa
subclasse.
• Faça todas as validações necessárias no programa.
• O saldo da conta precisa estar formatado com 2 casas decimais.
* */
fun main(){
    open class ContaBancaria(val nomeTitular:String, var saldoConta: Double){
        open fun depositar(valor:Double){
            saldoConta += valor
            println("Depósito realizado no valor de R$ ${"%.2f".format(valor)}")
            println("------------------------------------------------")
        }

        open fun sacar(valor:Double){
            if (valor > saldoConta) {
                println("Não é possível realizar a operação.\nO valor do saque é superior ao saldo da conta\nSaldo da conta R$ ${"%.2f".format(saldoConta)}")
            } else{
                saldoConta -= valor
                println("Saque realizado no valor de R$ ${"%.2f".format(valor)}")
            }
        }

        open fun exibirInformacoes(){
            println("Informações sobre a Conta Bancária:")
            println("Titular da Conta: R$ $nomeTitular")
            println("Saldo da Conta: R$ ${"%.2f".format(saldoConta)}")
            println("------------------------------------------")
        }

    }

    class ContaCorrente(nomeTitular: String, saldoConta: Double): ContaBancaria(nomeTitular, saldoConta){
        // toda vez que um cliente saca dinheiro é descontado uma taxa de 5.0
        val taxaOperacao: Double = 5.0

        override fun sacar(valor: Double) {
            if (valor > saldoConta) {
                println("Não é possível realizar a operação.\nO valor do saque é superior ao saldo da conta\nSaldo da conta R$ ${"%.2f".format(saldoConta)}")
                println("-----------------------------------------------")
            } else{
                saldoConta = saldoConta - (valor + taxaOperacao)
                println("Saque de R$ ${"%.2f".format(valor)}")
                println("Cobrança de taxa de operação: R$ ${"%.2f".format(taxaOperacao)}")
                println("-----------------------------------------------")
            }
        }

        override fun exibirInformacoes() {
            println("Informações sobre a Conta Corrente")
            println("Titular da Conta Corrente: $nomeTitular")
            println("Saldo da Conta Corrente: R$ ${"%.2f".format(saldoConta)}")
            println("------------------------------------------")

        }
    }

    class ContaPoupanca(nomeTitular: String, saldoConta: Double): ContaBancaria(nomeTitular, saldoConta){
        val rendimento: Double = 0.02
        override fun depositar(valor: Double) {
            saldoConta += valor + (valor*rendimento)
            println("Depósito realizado no valor de R$ ${"%.2f".format(valor)}")
            println("Rendimento de R$ ${"%.2f".format(valor*rendimento)}")
            println("-----------------------------------------------")
        }

        override fun exibirInformacoes() {
            println("Informações sobre a Conta Poupança")
            println("Titular da Conta Poupança: $nomeTitular")
            println("Saldo da Conta Poupança: R$ ${"%.2f".format(saldoConta)}")
            println("------------------------------------------")
        }

    }

    //Cliente com conta corrente. Obs: Tentativa de Saque Superior ao Valor da Conta
    println("Cliente 01")
    val cliente01 = ContaCorrente("Danielly Amanda", 500.00)
    cliente01.sacar(2000.0)
    cliente01.exibirInformacoes()

    // Multiplos saques
    println("Cliente 02")
    val cliente02 = ContaCorrente("Armando Ferreira", 12300.00)
    cliente02.sacar(500.0)
    cliente02.sacar(130.00)
    cliente02.sacar(680.00)
    cliente02.sacar(986.00)
    cliente02.exibirInformacoes()

    //Cliente com a conta poupança
    println("Cliente 03")
    val cliente03= ContaPoupanca("Rosa Assunção", 6000.00)
    cliente03.depositar(100.0)
    cliente03.depositar(500.00)
    cliente03.exibirInformacoes()



}

