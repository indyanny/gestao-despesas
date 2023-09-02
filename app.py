class Despesa:
    def _init_(self, descricao, categoria, valor):
        self.descricao = descricao
        self.categoria = categoria
        self.valor = valor


class ControleDespesas:
    def _init_(self):
        self.despesas = []

    def adicionar_despesas(self, despesas):
        self.despesas.append(despesas)

    def listar_despesas(self):
        if self.despesas:
            for index, despesa in enumerate(self.despesas, start=1):
                print("-"*30)
                print(f"{index} . Descrição: {despesa.descricao}")
                print(f"Categoria: {despesa.categoria}")
                print(f"Valor: R${despesa.valor}")
                print("-"*30)

        else:
            print("Nenhuma despesa foi cadastrada.")

if _name_ == "_main_":
    controle = ControleDespesas()

    while True:
        print("1. Adicionar Despesa.")
        print("2. Listar Despesas.")
        print("3. Sair")
        opcao = input("Escolha a opção desejada:")

        if opcao == "1":
            descricao = input("Qual a descrição da despesa?")
            categoria = input("Qual a categoria da despesa?")
            valor = input("Qual o valor da despesa?")
            despesa = Despesa(descricao, categoria, valor)
            controle.adicionar_despesas(despesa)
            print("-"*30)
            print("Despesa adicionada com sucesso")
            print("-"*30)

        elif opcao == "2":
            print("Lista de despesas:")
            controle.listar_despesas()

        elif opcao == "3":
            print("Finalizando")
            break

        else:
            print("Opção inválida, tente novamente")