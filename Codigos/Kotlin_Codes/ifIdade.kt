// Scanner serve para a entrada de dados via teclado
import java.util.Scanner // Java

fun main(){
    // só pode ter um fun main no arquivo
    val scanner = Scanner(System.`in`) // criando o obj scanner
    // colocamos o essa variavel scanner com s minusculo diferente do Scanner do import com S maisuclo

    val idade: Int
    println("Digite a sua idade: ")
    idade = scanner.nextInt()

    if(idade < 18){
        println("Ainda faltam ${18 - idade} anos para sua maioridade")
    } else if (idade >= 18 && idade < 130) {
        println("Você é maior de idade")
    }else {
        println("Você é o ser humano mais velho do Brasil!")
    }
}