number = int(input("Enter a number: "))


def factorial(n):
    fat = 1

    for i in range(n, 1, -1):
        fat = fat * i

    return fat


count = 1
while True:
    if factorial(count) == number:
        print(f"{number} = {count}!")
        break
    elif factorial(count) < number:
        count += 1
    else:
        print(f"{count - 1}! < {number} < {count}!")
        break
