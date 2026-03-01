from linked_list import LinkedList


def print_status(title, lst: LinkedList):
    print(f"\n{title}")
    print("Lista:", str(lst))
    print("Tamanho:", len(lst))


def test_append():
    print("=== Teste: Inserções no final ===")
    lst = LinkedList()
    print_status("Inicial", lst)
    lst.append(8)
    print_status("Após inserir 8 no final", lst)
    lst.append(6)
    print_status("Após inserir 6 no final", lst)
    lst.append(10)
    print_status("Após inserir 10 no final", lst)
    return lst


def test_insert():
    print("\n=== Teste: Inserções em qualquer posição ===")
    lst = LinkedList()
    lst.insert(0, 1)
    print_status("Após inserir 1 em index 0 (vazia)", lst)
    lst.insert(1, 3)
    print_status("Após inserir 3 no fim (index == size)", lst)
    lst.insert(1, 2)
    print_status("Após inserir 2 no meio (index 1)", lst)
    lst.insert(0, 0)
    print_status("Após inserir 0 no início (index 0)", lst)
    lst.insert(len(lst), 4)
    print_status("Após inserir 4 no fim", lst)
    return lst


def test_get_set_item(lst: LinkedList):
    print("\n=== Teste: __getitem__ e __setitem__ ===")
    print_status("Estado atual", lst)
    try:
        print("Elemento na posição 0:", lst[0])
        print("Elemento na posição 2:", lst[2])
    except IndexError as e:
        print("IndexError ao acessar:", e)

    try:
        lst[2] = 99
        print_status("Após setitem [2]=99", lst)
    except IndexError as e:
        print("IndexError ao atribuir:", e)

    try:
        _ = lst[-1]
    except IndexError as e:
        print("IndexError esperado ao acessar índice negativo:", e)

    try:
        _ = lst[len(lst)]
    except IndexError as e:
        print("IndexError esperado ao acessar índice >= tamanho:", e)


def test_index_lookup(lst: LinkedList):
    print("\n=== Teste: index(valor) ===")
    try:
        print("Índice do valor 99:", lst.index(99))
    except ValueError as e:
        print("ValueError inesperado ao buscar 99:", e)

    try:
        print("Índice do valor 123 (inexistente):", lst.index(123))
    except ValueError as e:
        print("ValueError esperado ao buscar inexistente:", e)


def test_removals():
    print("\n=== Teste: Remoções ===")
    lst = LinkedList()
    for x in [1, 2, 3, 4]:
        lst.append(x)
    print_status("Inicial (1->2->3->4)", lst)

    try:
        lst.remove(3)
        print_status("Após remover 3 (meio)", lst)
    except ValueError as e:
        print("ValueError inesperado ao remover 3:", e)

    try:
        lst.remove(1)
        print_status("Após remover 1 (head)", lst)
    except ValueError as e:
        print("ValueError inesperado ao remover 1:", e)

    try:
        lst.remove(4)
        print_status("Após remover 4 (tail)", lst)
    except ValueError as e:
        print("ValueError inesperado ao remover 4:", e)

    try:
        lst.remove(999)
    except ValueError as e:
        print("ValueError esperado ao remover inexistente:", e)

    empty_list = LinkedList()
    try:
        empty_list.remove(1)
    except ValueError as e:
        print("ValueError esperado ao remover em lista vazia:", e)
    return lst


def test_full_flow():
    print("\n=== Fluxo completo ===")
    lst = LinkedList()
    print_status("Inicial", lst)
    for x in [10, 20, 40]:
        lst.append(x)
    print_status("Após inserir 10, 20, 40 no fim", lst)

    lst.insert(2, 30)
    print_status("Após inserir 30 em index 2", lst)

    print("Valor em [1]:", lst[1])
    lst[1] = 25
    print_status("Após setitem [1]=25", lst)

    print("Index do valor 30:", lst.index(30))

    lst.remove(10)
    print_status("Após remover 10 (head)", lst)
    lst.remove(30)
    print_status("Após remover 30 (meio)", lst)
    lst.remove(40)
    print_status("Após remover 40 (tail)", lst)
    print_status("Final", lst)


if __name__ == "__main__":
    final_list = test_append()
    multi_pos_list = test_insert()
    test_get_set_item(multi_pos_list)
    test_index_lookup(multi_pos_list)
    list_after_removals = test_removals()
    test_full_flow()
