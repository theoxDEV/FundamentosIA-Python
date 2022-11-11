class Produto:
    def __init__(self, nome: str, preco: float, quantidadeEstoque: int):
        self._nome = nome
        self._preco = preco
        self._quantidadeEstoque = quantidadeEstoque

    def verificarProdutoEmEstoque(self, quantidadePedido: int):
        if(self._quantidadeEstoque < quantidadePedido):
            print("Produto fora de estoque")
            pass

    def imprimir(self):
        print(self._nome)
        print(self._preco)
        print(self._quantidadeEstoque)