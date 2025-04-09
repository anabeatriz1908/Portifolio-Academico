fun main(){
    var name: String = "Ana Beatriz" // ouuuu
    var nameSeparado: String
    nameSeparado = "Beatriz Ana"
    println(nameSeparado)
    
    var aniversario: Int  = 2005
    
    println(name)
    println(aniversario)
    println("Ola $name estamos em $aniversario") //concatenação com $
    println("Hello Word")
    println("$name tem ${name.length} letras")

    var numeroFlot: Float
    numeroFlot = 6.66F // é necessãrio colocar o F para numeros float, senão dá erro
    var numeroDoule: Double = 6.66
    println(numeroFlot)
    println(numeroDoule)

    var idade = 19
    ++idade // aumenta só um
    println("Seu nome é $name e sua idade é $idade")

    idade += 20 // precisa ficar 20 + 20 = 40
    println("Idade daqui a 20 anos: $idade anos")
}

/*não é possivel alterar uma variavel var para val ou vice-versa. Como:
var name - para > val name. Ou é val ou é var
*/


