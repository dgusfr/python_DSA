novos_itens = [
    ("eletronicos", "fone de ouvido"),
    ("livros", "python basico"),
    ("eletronicos", "mouse"),
    ("eletronicos", "fone de ouvido"), # O fornecedor mandou duplicado!
    ("escritorio", "caneta")
]

catalogo_atual = {
    "eletronicos": {"teclado", "monitor"},
    "livros": {"algoritmos"}
}


def atualizar_catalogo(catalogo, novos_itens):
