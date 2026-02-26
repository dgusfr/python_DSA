number_a = int(input("Digite o primeiro número inteiro positivo: "))
number_b = int(input("Digite o segundo número inteiro positivo: "))


def friend_number(a, b):
    total_a = 0
    total_b = 0

    for i in range(1, a):
        if a % i == 0:
            total_a += i

    for j in range(1, b):
        if b % j == 0:
            total_b += j

    if total_a == b and total_b == a:
        print(f"Os números {a} e {b} são amigos.")
    else:
        print(f"Os números {a} e {b} não são amigos.")


friend_number(number_a, number_b)
