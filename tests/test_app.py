import pytest
from src.app import adicionar_gasto, calcular_total, listar_gastos

def test_adicionar_gasto():
    adicionar_gasto("Almoço", 20)
    assert listar_gastos()[-1]["nome"] == "Almoço"

def test_valor_negativo():
    with pytest.raises(ValueError):
        adicionar_gasto("Erro", -10)

def test_calcular_total():
    adicionar_gasto("Teste", 10)
    total = calcular_total()
    assert total >= 10