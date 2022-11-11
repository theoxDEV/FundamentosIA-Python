class Livro:
    def __init__(self, nomeDoLivro: str, quantidadeEmprestimo: int):
        self._nomeDoLivro = nomeDoLivro
        precoEmprestimo = self.verificarValorDoLivro(nomeDoLivro)
        self._quantidadeEmprestimo = quantidadeEmprestimo
        self.verificarLivroEmEstoque(quantidadeEmprestimo)


    def verificarLivroEmEstoque(self, quantidadeEmprestimo: int):
        #Valor fixo de estoque de livros
        quantidadeEstoque = 10;

        if(quantidadeEmprestimo > quantidadeEstoque):
            print("Livro fora de estoque !")
            pass


    def verificarValorDoLivro(self, nomeDoLivro: str):
        if (nomeDoLivro == "Senhor dos Anéis"):
            return 7.99
        elif (nomeDoLivro == "One Piece"):
            return 5.99
        elif (nomeDoLivro == "A ilha perdida"):
            return 2.99
        elif (nomeDoLivro == "Tosco"):
            return 4.99