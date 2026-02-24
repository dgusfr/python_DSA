novos_itens = [
    ("eletronicos", "fone de ouvido"),
    ("livros", "python basico"),
    ("eletronicos", "mouse"),
    ("eletronicos", "fone de ouvido"),
    ("escritorio", "caneta"),
]

catalogo_atual = {"eletronicos": {"teclado", "monitor"}, "livros": {"algoritmos"}}


def atualizar_catalogo(catalogo, novos_itens):
    for categoria, item in novos_itens:
        if categoria not in catalogo:
            catalogo[categoria] = set()
        catalogo[categoria].add(item)
    return catalogo


print(atualizar_catalogo(catalogo_atual, novos_itens))
