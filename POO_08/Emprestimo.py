from Livro import Livro
from Pessoa import Pessoa

class Emprestimo:
    def __init__(self, livros: Livro, cliente: Pessoa):
        self._livros = livros
        self._cliente = cliente
        self._valorTotalDoEmprestimo = self.valorTotalDoEmprestimo(livros)
        self.imprimir()


    def valorTotalDoEmprestimo(self, livros: Livro):
        #Definindo valor total
        valorTotalEmprestimo = 0;

        for livro in livros:
            valorTotalEmprestimo += livro.verificarValorDoLivro(livro._nomeDoLivro)

        return valorTotalEmprestimo


    def imprimir(self):
        print(self._valorTotalDoEmprestimo)
