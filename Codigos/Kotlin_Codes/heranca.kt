// Classe base/Super
open class Animal (val nome: String, val tipoAnimal: String, val tipoPele: String){
    open fun emiteSom() {  // isso é u metodo dentro de uma função
        println("Silêncio! O animal está fazendo um som!!")
    }
    open fun caracteristicas(){
        println("Seja Bem-Vinda(o) $tipoAnimal!!")
        println("O animal tem uma pele e cor genérica")
    }
}

// Classe Devirada/Filha
class Hiena(nome: String, tipoAnimal: String, tipoPele: String): Animal(nome, tipoAnimal, tipoPele ){
    // vamos reescrever/sobreescrever um metodo
    override fun emiteSom() {
        println("------------------------------------------------------------------------------")
        println("A $tipoAnimal $nome faz: HAHAHA HIHIHI")

    }

    override fun caracteristicas() {
        emiteSom()
        println("Seja Bem-Vinda(o) $tipoAnimal!!")
        println("A $tipoAnimal tem $tipoPele e manchinhas")
        println("------------------------------------------------------------------------------")
    }
    // O OVERRIDE ESTÁ SOBREESCREVENDO O METODO DA CLASS MÃE
}

class Crocodilo(nome:String, tipoAnimal: String, tipoPele: String): Animal(nome, tipoAnimal, tipoPele) {
    override fun emiteSom() {
        println("------------------------------------------------------------------------------")
        println("O $tipoAnimal $nome faz: ROAAAAAR ROOOR ROOOOOR")

    }
    override fun caracteristicas() {
        emiteSom()
        println("Seja Bem-Vinda(o) $tipoAnimal!!")
        println("O $tipoAnimal tem $tipoPele e pele verde")
        println("------------------------------------------------------------------------------")
    }
}

class Orca(nome:String, tipoAnimal: String, tipoPele: String): Animal(nome, tipoAnimal, tipoPele){
    override fun emiteSom() { // polimorfismo
        println("------------------------------------------------------------------------------")
        println("A $tipoAnimal $nome faz: BLUB BLUB BLUB")
    }

    override fun caracteristicas() {
        emiteSom()
        println("Seja Bem-Vinda(o) $tipoAnimal!!")
        println("A $tipoAnimal tem $tipoPele e é preta e branca")
        println("------------------------------------------------------------------------------")
    }
}

fun main() {
    val hiena = Hiena("Janete", tipoAnimal = "Hiena", tipoPele = "pelos")
    hiena.caracteristicas()

    val crodilo = Crocodilo("Catarina", tipoAnimal = "Crocodilo", tipoPele = "escamas")
    crodilo.caracteristicas()

    val orca = Orca(nome = "Bárbara", tipoAnimal = "Orca", tipoPele = "barbatanas")
    orca.caracteristicas()
}