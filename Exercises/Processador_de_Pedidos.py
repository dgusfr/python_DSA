"""
Crie uma função em Python chamada calcular_faturamento_entregue que receba essa lista e retorne apenas o valor total (soma) de todos os pedidos que têm o status "entregue".
"""

pedidos = [
    {"id": 1, "status": "pendente", "itens": [{"preco": 100, "qtd": 1}]},
    {
        "id": 2,
        "status": "entregue",
        "itens": [{"preco": 50, "qtd": 2}, {"preco": 200, "qtd": 1}],  # Total: 300
    },
    {"id": 3, "status": "cancelado", "itens": [{"preco": 500, "qtd": 1}]},
    {"id": 4, "status": "entregue", "itens": [{"preco": 10, "qtd": 10}]},  # Total: 100
]


def calcular_faturamento_entregue(lista_pedidos):
    valor_total = 0
    for pedido in lista_pedidos:
        if pedido.get("status") == "entregue":
            for item in pedido.get("itens", []):
                valor_total = valor_total + (item.get("preco", 0) * item.get("qtd", 0))

    return valor_total


print(
    f"O valor total dos pedidos entregues é R$ {calcular_faturamento_entregue(pedidos)}"
)
