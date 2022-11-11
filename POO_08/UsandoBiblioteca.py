from Emprestimo import Emprestimo
from Livro import Livro
from Pessoa import Pessoa

#Pessoa
pessoa1 = Pessoa('Matheus Nascimento', '(65) 3488-2363', 'berneice8675@uorak.com')

# appending instances to listaDeContatos

listaDeLivros = []
listaDeLivros.append(Livro('Senhor dos Anéis', 3))
listaDeLivros.append(Livro('Tosco', 9))

#Emprestimo
emprestimo1 = Emprestimo(listaDeLivros, pessoa1)