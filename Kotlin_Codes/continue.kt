/*
Crie um programa que conta de 1 a 20, mas ignora os números múltiplos de 3 usando continue.

Regras:
O programa deve usar um while ou for.
Sempre que encontrar um número múltiplo de 3, ele deve ignorar esse número e continuar para o próximo.
Os outros números devem ser impressos normalmente.
 */
fun main(){
    var num: Int = 0
    println("Vamos contar!")

    while (num <= 20){
        if (num % 3 == 0){
            num++
            continue

        }
        println("Contando $num...")
        num++
    }
}