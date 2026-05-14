from src.app import (
    adicionar_gasto,
    calcular_total,
    consultar_cotacao_dolar,
    listar_gastos,
    remover_gasto,
)


def test_adicionar_gasto():
    adicionar_gasto("Mercado", 100)
    assert {"nome": "Mercado", "valor": 100} in listar_gastos()


def test_calcular_total():
    adicionar_gasto("Transporte", 20)
    assert calcular_total() >= 20


def test_remover_gasto():
    adicionar_gasto("Internet", 80)
    remover_gasto("Internet")
    assert {"nome": "Internet", "valor": 80} not in listar_gastos()


class RespostaMock:
    def raise_for_status(self):
        pass

    def json(self):
        return {
            "USDBRL": {
                "name": "Dólar Americano/Real Brasileiro",
                "bid": "5.50",
                "create_date": "2026-05-14 10:00:00",
            }
        }


def test_consultar_cotacao_dolar(monkeypatch):
    def mock_get(url, timeout):
        return RespostaMock()

    monkeypatch.setattr("requests.get", mock_get)

    cotacao = consultar_cotacao_dolar()

    assert cotacao["moeda"] == "Dólar Americano/Real Brasileiro"
    assert cotacao["valor"] == 5.50
    assert cotacao["data"] == "2026-05-14 10:00:00"