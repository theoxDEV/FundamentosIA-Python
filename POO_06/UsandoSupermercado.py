from Supermercado import Supermercado
from Produto import Produto
from Pedido import Pedido

#Produto
produto1 = Produto("Banana", 3.99, 10)

#Pedido
pedido1 = Pedido(produto1, 50, "Cartão")

#Supermercado
mercado1 = Supermercado(pedido1)