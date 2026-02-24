vendas = [
    {"categoria": "eletronicos", "valor": 1200},
    {"categoria": "livros", "valor": 40},
    {"categoria": "eletronicos", "valor": -800},  # Outro eletrônico!
    {"categoria": "roupas", "valor": 200},
    {"categoria": "livros", "valor": 60},
    {"categoria": "alimentos", "valor": 50},
]


def agrupar_vendas_por_categoria(lista_vendas):
    relatorio = {}
    for venda in lista_vendas:
        categoria = venda.get("categoria")
        valor = venda.get("valor", 0)

        if categoria not in relatorio:
            relatorio[categoria] = valor
        else:
            relatorio[categoria] += valor

    return relatorio


print(agrupar_vendas_por_categoria(vendas))


# Saida esperada:
# {
#     "eletronicos": 2000, # 1200 + 800
#     "livros": 100,       # 40 + 60
#     "roupas": 200,
#     "alimentos": 50
