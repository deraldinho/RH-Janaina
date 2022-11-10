class Funcionario:

    def __int__(self):
        self.id
        self.nome
        self.setor
        self.salario

    def criar_funcionario(self, nome, setor, salario):
        try:
            nome = str(nome)
            setor = str(setor)
            salario = float(salario)

        except:
            pass
        else:
            pass


class Interface():

    def __init__(self):
        self.control = ''
        self.funci = Funcionario()

    def loop(self):
        self.home()
        while True:
            break

    def home(self):
        print()


if __name__ == '__main__':
    screen = Interface()
    screen.loop()
