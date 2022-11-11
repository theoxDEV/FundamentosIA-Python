class Contato:
    def __init__(self, nome: str, telefone: str, email: str):
        self._nome = nome
        self._telefone = telefone
        self._email = email

    def imprimir(self):
        print(self._nome)
        print(self._telefone)
        print(self._email)