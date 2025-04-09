/*Crie variáveis para salvar os seguintes dados de uma pessoa:

1. nome
2. sobrenome
3. peso
4. altura
5. possui avião ?

Em seguida imprima esse valor na tela do computador
*/
import java.util.Scanner
fun main () {
    val scanner = Scanner(System.`in`)

    println("Digite seu nome: ")
    val nome: String = scanner.nextLine()

    println("Digite seu sobrenome: ")
    val sobrenome: String = scanner.nextLine()

    println("Você possui avião: ")
    val possuiAviao: String = scanner.nextLine()

    println("Digite seu peso: ")
    val peso: Float = scanner.nextFloat()

    println("Digite sua altura: ")
    val altura: Float = scanner.nextFloat()



    println("-----------------------------------")
    println("Suas informações: ")
    println("Nome: $nome $sobrenome")
    println("Peso: $peso kg")
    println("Altura: $altura m")
    println("Avião: $possuiAviao")
    println("-----------------------------------")

}