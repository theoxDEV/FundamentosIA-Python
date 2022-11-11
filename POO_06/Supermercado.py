from Pedido import Pedido

class Supermercado:
    def __init__(self, pedido: Pedido):
        self._pedido = pedido

    def imprimir(self):
        print(self._pedido.imprimir())