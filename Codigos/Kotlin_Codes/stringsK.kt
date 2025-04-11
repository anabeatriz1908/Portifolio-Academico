fun main(){
    var txt = "Hoje é sexta-feira, dia da maldade"
    // textos ocupam espaço da memória
    println(txt[0]) // exibe a letra 'H'
    // Indices vão de 0 a n
    println(txt[4]) // printa o espaço em branco

    var txt2 = "Abracadara - Lady Gaga"
    println("O texto tem: ${txt2.length} caracteres")

    var txt3 = "Gatos e Passáros"
    println(txt3.uppercase())// sai tudo em minusculo
    println(txt3.lowercase())

    var primeiroNome = "Ana "
    var segundoNome = "Beatriz "
    println(primeiroNome.plus(segundoNome)) // ao inves de colocar o +, podemos usar o plus

    var terceiroNome = "Silva "
    var quartoNome = "Santos"
    println(primeiroNome.plus(segundoNome).plus(terceiroNome).plus(quartoNome)) // nome Completo

    // Interpolação ---> $
    var firstName = "Marcela"
    var lastName = "Ribeiro"
    println("My name is: $firstName ${lastName.uppercase()}")
    // não precisa colocar { } quando não estivermos trabalhanco com metodos como upper, lower, lenght
    // não é uma boa prática posso usar tanto ${variavel} como $variavel


}