fun main (){
    // When é o swtich case do java adaptado para o Kotlin
    val day =  5
    val result = when(day){
        1 -> "Segunda"
        2 -> "Terça"
        3 -> "Quarta"
        4 -> "Quinta"
        5 -> "Sexta"
        6 -> "Sábado"
        7 -> "Domingo"
        else -> "Dia não inventado"
    }
    println("Hoje é $result")

}