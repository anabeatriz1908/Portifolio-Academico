/*
Sistema de Funcionários: Você foi contratado pela empresa IMPACTA DEVS para
desenvolver o novo sistema de funcionários da empresa. Para isso as seguintes orientações devem
ser seguidas:
• Crie a classe Funcionários com os seguintes atributos: nome do funcionário e salário.
Também deve ser implementado o método exibirInformacoes( ) responsável por imprimir o
nome e salário de cada funcionário.
• Crie a subclasse Gerente que herda de Funcionário e possui o atributo bônus: Double. O
salário total do gerente deve considerar o bônus.
• Crie a subclasse Desenvolvedor que herda de funcionário e possui o atributo
linguagemProgramacao: String.
• Aplique o polimorfismo no método exibirInformacoes( ) nas subclasses.
• Por fim crie uma lista com 2 funcionários, 2 gerentes e 2 desenvolvedores, e chame
exibirInformacoes() para cada um deles.
*/
fun main(){
    open class Funcionarios(val nomeFuncionario:String, val salario:Double){
        open fun exibirInformacoes() {
            println("Nome do Funcionário: $nomeFuncionario")
            println("Salário do Funcionário: ${"%.2f".format(salario)}")
            println("---------------------------------------------")
        }
    }
    class Gerente (nomeFuncionario:String, salario:Double, val bonus: Double): Funcionarios(nomeFuncionario, salario){
        val salario_gerente = salario + (salario * (bonus/100))

        override fun exibirInformacoes() {
            println("Nome do Gerente: $nomeFuncionario")
            println("Salário do Gerente: ${"%.2f".format(salario_gerente)}")
            println("---------------------------------------------")
        }
    }

    class Desenvolvedor(nomeFuncionario:String, salario:Double, val linguagemProgramacao:String): Funcionarios(nomeFuncionario, salario){
        override fun exibirInformacoes() {
            println("Nome do Desenvolvedor: $nomeFuncionario")
            println("Salário do Desenvolvedor: ${"%.2f".format(salario)}")
            println("Linguagem de programação que usa: $linguagemProgramacao")
            println("---------------------------------------------")
        }
    }

    val gerente01 = Gerente("Adriana de Melo", 2000.0, 15.0)
    gerente01.exibirInformacoes()
    val gerente02 = Gerente("Beatriz Costa", 3000.0, 20.0)
    gerente02.exibirInformacoes()
    val desenvolvedor01 = Desenvolvedor("Ana Santos", 10000.0, "Kotlin")
    desenvolvedor01.exibirInformacoes()
    val desenvolvedor02 = Desenvolvedor("Carla Andrade", 5000.0, "Lua")
    desenvolvedor02.exibirInformacoes()
    val funcionario01 = Funcionarios("Diana Machado", 2500.0)
    funcionario01.exibirInformacoes()
    val funcionario02 = Funcionarios("Eliana Paiva", 6000.0)
    funcionario02.exibirInformacoes()

}