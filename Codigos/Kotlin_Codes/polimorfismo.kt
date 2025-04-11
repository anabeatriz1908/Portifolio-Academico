/*
Permite que diferentes classes sejam tratadas como instancias da mesma classe base
 */

// classe base
open class Filmes(val titulo:String, val ano:Int){
    open fun descricao ():String {
        return "Filme: $titulo \nAno de Publicação: $ano"
    }

}

class FilmeTerror(titulo: String, ano: Int, val nota: Int): Filmes(titulo, ano){
    override fun descricao(): String { //POLIMORFISMO
        return "${super.descricao()} \nNota: $nota"
    }
}

class FilmeAcao(titulo: String, ano: Int, val acrobacia: Int): Filmes(titulo, ano){
    override fun descricao(): String { //POLIMORFISMO
        return "${super.descricao()} \nNúmero de acrobacias: $acrobacia"
    }
}

class FilmeDramaHistorico(titulo: String, ano: Int, val premios: String): Filmes(titulo, ano){
    override fun descricao(): String {
        return "${super.descricao()} \nMerece todos os prêmios que ganhou e muito mais? $premios"
    }
}

fun main(){
    val ListadeFilmes : List <Filmes> = listOf(
        FilmeTerror("A Bruxa", 2015, 5),
        FilmeAcao("Alerta Vermelho", 2020, 52),
        FilmeDramaHistorico("Ainda Estou Aqui", 2024, "Simmm e muito mais!!!"),
        FilmeTerror("O Iluminado", 1980, 5),
        FilmeAcao("Batman: O Cavalheiro das Trevas", 2008, 68),
        FilmeDramaHistorico("Hoje eu quero voltar sozinho",2014,"Simmm!!")

    )
   // println(ListadeFilmes) // EndereÇo de memorío
    for (filme in ListadeFilmes){
        println(filme.descricao())
        println("-----------------------------------------")
    }



}

