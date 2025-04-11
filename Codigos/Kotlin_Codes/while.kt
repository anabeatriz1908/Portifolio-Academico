import java.util.Scanner

fun main (){
    val scanner = Scanner(System.`in`)
    var numero: Int

    println("Digite um número par (impar para sair)")
    numero = scanner.nextInt()

    while (numero % 2 == 0){
        println("Você digitou $numero")

        println("Digite um número par (impar para sair)")
        numero = scanner.nextInt()
        println("------------------------------------")


    }
}