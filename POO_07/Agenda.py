from Contato import Contato

class Agenda:
    def __init__(self, contatos: Contato):
        self._contatos = contatos
        self.imprimir(contatos)

    def imprimir(self, contatos):
        for contato in contatos:
            print(contato._nome,
                  contato._email,
                  contato._telefone)