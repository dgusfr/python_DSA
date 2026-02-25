number_lines = int(input("Digite o número de linhas do Triângulo de Floyd: "))


def print_floyd_triangle(n):
    num = 1

    # for externo para controlar o número de linhas
    for i in range(1, n + 1):
        # for interno para imprimir os números em cada linha
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        # quebra de linha
        print()


print_floyd_triangle(number_lines)
