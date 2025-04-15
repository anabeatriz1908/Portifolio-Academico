class LigaDaJustica(var name: String, var codinome: String, var poder: String, var nivelPoder: Int) {

    fun combateLuta(){
        println("O Héroi está treinando")
    }

    fun combateCrime(name: String){
        println("$name diz: Estou ocupado combatendo o crime")
    }
    fun superForca(){
        println("O héroi é forte!!")
    }

}

fun main() {
    val batgirl = LigaDaJustica("Barbara Gordon", "Batgirl", "Luta coropo a corpo e aparados tecnologicos", 7)
    val bigBarda = LigaDaJustica("Barda", "Big Barda", "Luta marciais e bastão de apokopolis", 10)
    println(bigBarda) // endereço de mémoria
    println("Onde está a Batgirl")
    println(batgirl.combateLuta())

    println("A Barda é forte?")
    println(bigBarda.superForca())

    println(bigBarda.combateCrime(bigBarda.codinome))

    println(batgirl.combateCrime(batgirl.name))

}

