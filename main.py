class Funcionario:

    def criar_funcionario(self, nome, setor, salario):
        try:
            nome = str(nome)
            setor = str(setor)
            salario = float(salario)
        except ValueError:
            return False
        else:
            self.funcionario['nome'] = nome;
            self.funcionario['setor'] = setor;
            self.funcionario['salario'] = salario;
            return self.funcionario

class Lista():

    def __int__(self):
        self.funcionario = Funcionario()
        self.lista=[]

    def cadastrar_funcionario(self, id):
        try:
            id = int(id)
        except ValueError:
            pass
        else:
            self.lista[id] = self.funcionario.criar_funcionario()



class Interface():

    def __init__(self):
        self.bem_vindo()

    def loop(self):
        while (True):
            if not self.home():
                break

    def bem_vindo(self):
        print('Bem-Vindo ao Controle de Funcionario da Janaina Lessa de Paula')
        print('*****************************************************************************')

    def home(self):
        if not self.menu_principal():
            return False
        else:
            return True

    def menu_principal(self):
        print('------------------------------ MENU PRINCIPAL -------------------------------')
        print('Escolha a Opção desejada: \n'
              '1-Cadastrar Funcionario\n'
              '2-Consultar Funcionarios(s)\n'
              '3-Remover Funcionarios\n'
              '4-Sair')

        try:
            controle = int(input('>>>'))
        except ValueError:
            print('Opção invalida')
            return True
        else:
            if controle == 1:
                self.menu_cadastro()
                return True
            elif controle == 2:
                return True
            elif controle == 3:
                return True
            elif controle == 4:
                return False
            else:
                print('Opção invalida')
                return True

    def menu_cadastro(self):
        print('------------------------ MENU Cadastrar Funcionario -------------------------')
        print(f'Código do Funcionario ')

    def menu_consulta(self):
        print('------------------------------ MENU PRINCIPAL -------------------------------')
        print('Escolha a Opção desejada: \n'
              '1-Consultar Todos os Funcionarios\n'
              '2-Consultar Funcionarios por ID\n'
              '3-Consultar Funcionarios por setor\n'
              '4-Retornar')
        try:
            controle = int(input('>>>'))
        except ValueError:
            print('Opção invalida')
            return True
        else:
            if controle == 1:
                return True
            elif controle == 2:
                return True
            elif controle == 3:
                return True
            elif controle == 4:
                return False
            else:
                print('Opção invalida')
                return True

    def menu_remocao(self):
        pass


if __name__ == '__main__':
    screen = Interface()
    screen.loop()
