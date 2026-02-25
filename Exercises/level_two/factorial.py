number = int(input("Enter a number: "))


def fatorial(n):
    fat = 1

    for i in range(n, 1, -1):
        fat = fat * i

    return fat


print(fatorial(number))
