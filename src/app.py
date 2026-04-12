gastos = []

def adicionar_gasto(nome, valor):
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")
    gastos.append({"nome": nome, "valor": valor})

def listar_gastos():
    return gastos

def calcular_total():
    return sum(g["valor"] for g in gastos)

def remover_gasto(nome):
    global gastos
    gastos = [g for g in gastos if g["nome"] != nome]

def menu():
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Total gasto")
        print("4 - Remover gasto")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do gasto: ")
            valor = float(input("Valor: "))
            try:
                adicionar_gasto(nome, valor)
                print("Gasto adicionado!")
            except ValueError as e:
                print(e)

        elif opcao == "2":
            for g in listar_gastos():
                print(f"{g['nome']} - R$ {g['valor']}")

        elif opcao == "3":
            print(f"Total: R$ {calcular_total()}")

        elif opcao == "4":
            nome = input("Nome do gasto para remover: ")
            remover_gasto(nome)
            print("Removido!")

        elif opcao == "5":
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()