"""
Escreva um algoritmo que verifique se um número é perfeito. Um número perfeito é um número inteiro que é igual à soma de seus divisores exceto ele mesmo. Exemplo: o número 6, onde 1 + 2 + 3 = 6.
"""

number = int(input("Digite um número inteiro: "))


def is_perfect(n):
    if n < 2:
        return False

    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    if divisors_sum == n:
        return True
    else:
        return False


if is_perfect(number):
    print(f"{number} é um número perfeito.")
else:
    print(f"{number} não é um número perfeito.")
