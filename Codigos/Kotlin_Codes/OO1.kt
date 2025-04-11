/*
CLASSE -> molde para a criação de objeto.
É uma 'fabrica' de objetos

OBJETO -> abstração do mundo real
Instancia da classe

ATRIOBUTOS -> Caracteristicas dos objetos

MÉTODOS -> Ações dos objetos, comportamento

 */

fun main() {
    class LigaDaJustica {
        //atributos
        var name: String = "" // variavel string inicializada com 2 aspas
        var idade: Int = 0 // varivel numerica inicializada com zero
        var poder: String = ""
        var altura: Double = 0.0
    }
    // eu instancio o objeto no main

    val blackCanary = LigaDaJustica()
    blackCanary.name = "Dinah Lance"
    blackCanary.idade = 32
    blackCanary.poder = "Grito Super Sônico"
    blackCanary.altura = 1.80

    val blueBeetle = LigaDaJustica()
    blueBeetle.name = "Theodore Spethen Kord"
    blueBeetle.idade = 37
    blueBeetle.poder = "Escaravelho e Aparelhos Tecnologico"
    blueBeetle.altura = 1.85

    val boosterGold = LigaDaJustica()
    boosterGold.name = "Michael Jon Carter"
    boosterGold.idade = 35
    boosterGold.poder = "Traje e armas vindas do futuro"
    boosterGold.altura = 1.90

    //Exibindo informações sobre Black Canary
    println("Informações sobre a Black Canary")
    println("Nome verdadeiro: ${blackCanary.name} \nPoderes: ${blackCanary.poder} \nIdade: ${blackCanary.idade} \nAltura: ${blackCanary.altura}")
    println("------------------------------------------------------------")

    println("Informações sobre o Booster Gold")
    println("Nome verdadeiro: ${boosterGold.name} \nPoderes: ${boosterGold.poder} \nIdade: ${boosterGold.idade} \nAltura: ${boosterGold.altura}")
    println("------------------------------------------------------------")

    println("Informações sobre Blue Beetle")
    println("Nome verdadeiro: ${blueBeetle.name} \nPoderes: ${blueBeetle.poder} \nIdade: ${blueBeetle.idade} \nAltura: ${blueBeetle.altura}")
    println("------------------------------------------------------------")
    println(boosterGold) //Oo1Kt$main$LigaDaJustica@7a0ac6e3 aparece isso, o endereço de memoria
}