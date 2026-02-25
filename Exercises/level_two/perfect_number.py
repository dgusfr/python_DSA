number = int(input("Digite um número inteiro: "))


def is_perfect(n):
    if n < 2:
        return False

    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    return divisors_sum == n


if is_perfect(number):
    print(f"{number} é um número perfeito.")
else:
    print(f"{number} não é um número perfeito.")
