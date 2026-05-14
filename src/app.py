import json
import requests

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


def consultar_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()
    cotacao = dados["USDBRL"]

    return {
        "moeda": cotacao["name"],
        "valor": float(cotacao["bid"]),
        "data": cotacao["create_date"],
    }


def menu():
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Total gasto")
        print("4 - Remover gasto")
        print("5 - Consultar cotação do dólar")
        print("6 - Sair")

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
            cotacao = consultar_cotacao_dolar()

            print("\nCotação atual do dólar:")
            print(f"Moeda: {cotacao['moeda']}")
            print(f"Valor: R$ {cotacao['valor']:.2f}")
            print(f"Atualizado em: {cotacao['data']}")

        elif opcao == "6":
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()