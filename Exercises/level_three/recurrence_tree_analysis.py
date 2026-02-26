cont_b = 0
cont_g4 = 0


def g(n):
    global cont_b, cont_g4

    cont_b += 1
    if n == 4:
        cont_g4 += 1

    # Lógica da função g(n)
    if n == 0:
        return 1
    elif n == 1:
        return 3
    elif n < 4:
        return 2 * g(n - 1)
    else:
        return g(n - 1) + g(n - 2)


val_a = g(10)
cont_b = 0
g(12)
resp_b = cont_b

cont_g4 = 0  # Reset para contar apenas g(4) dentro de g(18)
g(18)
resp_c = cont_g4

print(f"a) Valor de g(10) = {val_a}")
print(f"b) Número de chamadas de g(12) = {resp_b}")
print(f"c) Número de chamadas de g(4) dentro de g(18) = {resp_c}")
