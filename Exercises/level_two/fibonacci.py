"""
Desenvolva um algoritmo que gere a sequência de Fibonacci até o n-ésimo termo, onde n é fornecido pelo usuário. A sequência de Fibonacci é definida como:
(0) = 0 para n = 0, F(1) = 1 para n = 1, e F(n) = F(n-1) + F(n-2) para n >= 2."
"""

number = int(input("Enter a number: "))


def fibonacci(n):
    if n < 0:
        return "Erro: Insira um numero positivo."
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    elif n >= 2:
        fib_sequence = [0, 1]

        for i in range(2, n + 1):
            next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_term)
        return fib_sequence


def print_fibonacci(fib_sequence):
    print("Sequência de Fibonacci até o n-ésimo termo:")
    for term in fib_sequence:
        print(term, end=" ")
    print()


print(fibonacci(number))
