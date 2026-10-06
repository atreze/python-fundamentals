from rich import print
from rich.panel import Panel


class Funcionario:
    """"
    Essa classe serve para definir nome, setor e cargo. No final, mostrar uma breve
    apresentação do funcionário com os paramêtros que foram passados no objeto.
    """
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __rich__(self):

        return f'Olá! me chamo [magenta2]{self.nome}[/] e sou [dark_orange]{self.cargo}[/] do setor de [medium_violet_red]{self.setor}[/] :alien: '

cadastro = Funcionario('Ana', 'Tecnologia', 'Desenvolvedora Júnior')
print(cadastro)
