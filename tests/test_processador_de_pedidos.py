import pytest
from Exercises.processador_de_pedidos import calcular_faturamento_entregue

# Estrutura: (Entrada, Saída Esperada)
cenarios_de_teste = [
    # Cenário 1: Caminho Feliz (Misto)
    (
        [
            {"status": "entregue", "itens": [{"preco": 10, "qtd": 1}]},
            {"status": "pendente", "itens": [{"preco": 50, "qtd": 1}]},
        ],
        10,
    ),
    # Cenário 2: Lista Vazia
    ([], 0),
    # Cenário 3: Nenhum entregue
    ([{"status": "cancelado", "itens": [{"preco": 100, "qtd": 1}]}], 0),
    # Cenário 4: Entregue mas sem itens
    ([{"status": "entregue", "itens": []}], 0),
]


@pytest.mark.parametrize("entrada, esperado", cenarios_de_teste)
def test_calcular_faturamento(entrada, esperado):
    resultado = calcular_faturamento_entregue(entrada)
    assert resultado == esperado
