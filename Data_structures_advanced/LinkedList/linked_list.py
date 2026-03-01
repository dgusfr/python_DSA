from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, data):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = data
        else:
            raise IndexError("list index out of range")

    def index(self, data):
        pointer = self.head
        indice = 0
        while pointer:
            if pointer.data == data:
                return indice
            pointer = pointer.next
            indice = indice + 1
        raise ValueError("{} is not in list".format(data))

    def _getnode(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("list index out of range")
        pointer = self.head
        for _ in range(index):
            if pointer is None:
                raise IndexError("list index out of range")
            pointer = pointer.next
        return pointer

    def insere_final_lista(self, data):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(data)
        else:
            self.head = Node(data)
        self._size = self._size + 1

    def insere_qualquer_posicao(self, index, data):
        if index < 0 or index > self._size:
            raise IndexError("list index out of range")

        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            anterior = self._getnode(index - 1)
            if anterior is None:
                raise IndexError("list index out of range")
            node.next = anterior.next
            anterior.next = node
        self._size = self._size + 1

    def remove(self, data):
        if self.head == None:
            raise ValueError("{} is not in list".format(data))
        elif self.head.data == data:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == data:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in list".format(data))

    def __repr__(self):
        r = ""
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
