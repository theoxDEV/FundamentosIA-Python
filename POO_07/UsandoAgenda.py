from Agenda import Agenda
from Contato import Contato

# creating list
listaDeContatos = []

# appending instances to listaDeContatos
listaDeContatos.append(Contato('Matheus Nascimento', '(65) 3488-2363', 'berneice8675@uorak.com'))
listaDeContatos.append(Contato('Luiz Augusto', '(92) 2628-1518', 'cristiana3408@uorak.com'))
listaDeContatos.append(Contato('Fernando Alvarenga', '(63) 3854-5016', 'roshan4566@uorak.com'))

agenda1 = Agenda(listaDeContatos);