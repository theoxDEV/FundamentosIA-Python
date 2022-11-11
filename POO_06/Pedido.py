from Produto import Produto

class Pedido:
    def __init__(self, itens: Produto, quantidadeItens: int, tipoDePagamento: str):
        self._itens = itens
        self._quantidadeItens = quantidadeItens
        self._tipoDePagamento = tipoDePagamento

        if not (Produto.verificarProdutoEmEstoque(itens, quantidadeItens)):
            print("Pedido inválido")

        if not (self.verificarFormaDePagamento()):
            pass


    def verificarFormaDePagamento(self):
        formasDePagamentoValidas = ["Dinheiro", "Cartão", "Cheque"]
        validaOuInvalida = "INVÁLIDA"

        if self._tipoDePagamento in formasDePagamentoValidas:
            print("Forma de pagamento VÁLIDA")
        else:
            print("Forma de pagamento INVÁLIDA")



    def imprimir(self):
        print(self._itens.imprimir())
        print(self._quantidadeItens)
        print(self._tipoDePagamento)
