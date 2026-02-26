"""
g = lambda n: 1 if n == 0 else 3 if n == 1 else 2 * g(n-1) if n < 4 else g(n-1) + g(n-2)
"""


def g(n):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    elif n < 4:
        return 2 * g(n - 1)
    else:
        return g(n - 1) + g(n - 2)


n = int(input("Digite um número inteiro não negativo: "))
result = g(n)
print(f"O resultado de g({n}) é: {result}")


# a) Qual é o valor numérico resultante da chamada g(10)?
# b) Quantas vezes a função g é chamada no total para concluir o cálculo de g(12)?
# c) Quantas vezes a sub-chamada g(4) é executada durante a árvore de resolução de g(18)?
