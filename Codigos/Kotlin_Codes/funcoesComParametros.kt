import java.util.Scanner
fun nameFunction(name:String, idade:Int){
    println("Bem-Vindo, $name " + "Silva Santos")
    println("A idade de $name é: $idade")
    println("----------------------------------------")

}
    fun somaFunction(num1:Int, num2:Int): Int{
    return (num1 + num2)
}

fun main(){
    nameFunction("Ana Beatriz", idade = 19)
    nameFunction(name = "Marcelo", idade = 32)

    val scanner = Scanner(System.`in`)
    println("Digite o primeiro número: ")
    val numero1: Int = scanner.nextInt()
    println("Digite o segundo número: ")
    val numero2: Int = scanner.nextInt()
    println("Soma: ${somaFunction(num1 = numero1, num2 = numero2)}")
    println("Soma: ${somaFunction(num1 = 10, num2 = 20)}")
}

