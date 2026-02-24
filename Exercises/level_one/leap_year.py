def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Exemplo de uso
year = int(input("Digite um ano: "))
if is_leap_year(year):
    print(f"{year} é um ano bissexto.")
else:
    print(f"{year} não é um ano bissexto.")
