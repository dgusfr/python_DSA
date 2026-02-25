"""
Considere a função matemática calc definida pela equação de somatório abaixo, onde n é um número inteiro não negativo:

calc(n) = ∑(i=0 to n) [4i + 5]

a) Escreva a função calc em Python de forma iterativa .
b) Escreva a função calc em Python de forma recursiva.

"""

number = int(input("Digite um número inteiro não negativo: "))


def calc_iterative(n):
    soma = 0
    if n < 0:
        return 0

    for i in range(n + 1):
        soma += 4 * i + 5
    return soma


def calc_recursive(n):
    if n < 0:
        return 0
    else:
        return (4 * n + 5) + calc_recursive(n - 1)


print(f"Resultado da função calc de forma iterativa: {calc_iterative(number)}")
print(f"Resultado da função calc de forma recursiva: {calc_recursive(number)}")
