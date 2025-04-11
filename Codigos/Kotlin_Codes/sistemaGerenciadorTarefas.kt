/*
Código Desenvolvido por Colegas

3- Você foi contratado pela USP, para criar um sistema gerenciador de matérias.
Crie uma classe Disciplina, que tem:
Atributos:
• Nome professor
• Nota (nota final)
• Número sala
• Linguagem
• Dia (recebe dia da semana)
Métodos:
• Codar( ), que exibe a linguagem e a nota do aluno na matéria
• Dia_da_aula( ), que recebe o dia da semana, faz uma verificação dos deles, se
for sexta, é dia da maldade, e exibe qual a sala e professor do dia
Depois, crie 2 subclasses que herdam da classe Disciplina
 */
open class Disciplina(val nomeProfessor: String, val nota: Double, val numSala: Int, val linguagem: String, val dia: String ){
    open fun codar(){
        println("Bem-vindo ao Sistema")
    }

    open fun diaAula(){
        println("Sala: $numSala \nProfessor: $nomeProfessor")
        if(dia == "Sexta"){
            println("Dia da Maldade!")
        }else{
            println("Hoje é dia normal")
        }
    }
}

class DesenvolvimentoWeb(nomeProfessor: String, nota: Double, numSala: Int, linguagem: String, dia: String): Disciplina(nomeProfessor, nota, numSala, linguagem, dia){
    override fun codar(){
        println("Linguagem: $linguagem \nNota Aluno: $nota")

    }

    override fun diaAula(){
        println("Sala: $numSala \nProfessor: $nomeProfessor")
        if(dia == "Segunda"){
            println("Dia da Web")
        }else if(dia == "Sexta"){
            println("Dia da Maldade!")
        }else{
            println("Dia Normal")
        }
    }

}

class DesenvolvimentoApi(nomeProfessor: String, nota:Double, numSala:Int, linguagem:String, dia:String): Disciplina(nomeProfessor, nota, numSala, linguagem, dia){
    override fun codar(){
        println("Linguagem: $linguagem \nNota Aluno: $nota")
    }

    override fun diaAula() {
        println("Sala: $numSala \nProfessor: $nomeProfessor")
        if(dia=="Terca"){
            println("Dia de Api")
        }else if(dia == "Sexta"){
            println("Dia da Maldade!")
        }else{
            println("Dia Normal")
        }
    }
}

fun main(){
    val disciplina01 = DesenvolvimentoApi(nomeProfessor="Vitor", nota=9.6, numSala=108, linguagem ="Java", dia = "Terca" )
    disciplina01.codar()
    disciplina01.diaAula()
    println("----------------------------------------------")
    val disciplina02 = DesenvolvimentoWeb(nomeProfessor = "Carlos", nota = 8.70, numSala = 170, linguagem = "Python", dia = "Sexta")
    disciplina02.codar()
    disciplina02.diaAula()
}
