number = int(input("Enter a number: "))


def fatorial(n):
    if n < 0:
        return "Erro: Insira um numero positivo."
    fat = 1

    for i in range(n, 1, -1):
        fat = fat * i

    return fat


print(fatorial(number))
