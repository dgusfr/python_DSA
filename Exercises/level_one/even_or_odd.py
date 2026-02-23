while True:
    number = int(input("Digite um numero inteiro:"))
    if number == -1:
        break
    else:
        if number % 2 == 0:
            print("O numero é par!")
        else:
            print("O numero é impar!")
