array = [1, 2, 3, 4, 5]


def reverse_list_out(lista):
    n = len(lista)
    nova_lista = []
    for i in range(n - 1, -1, -1):
        nova_lista.append(lista[i])
    return nova_lista
