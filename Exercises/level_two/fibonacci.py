number = int(input("Enter a number: "))


def fibonacci(n):
    if n < 0:
        return "Erro: Insira um numero positivo."

    fib_sequence = []

    if n == 0:
        fib_sequence = [0]
        return fib_sequence
    elif n == 1:
        fib_sequence = [0, 1]
        return fib_sequence
    elif n >= 2:
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_term)
    return fib_sequence


print(fibonacci(number))
