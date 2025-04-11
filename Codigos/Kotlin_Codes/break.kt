fun main(){
    // BREAK: forçar a interrupção do programa
    println("Vamos contar!")
    var num: Int = 1;
    while(num<= 10){
        println("Contando $num...")
        num++ // Na 5 interação do loop, o num será 05 e o loop será interrompido

        if (num == 5){
            println("Interrompendo contagem no número 5")
            break;
        }
    }
}