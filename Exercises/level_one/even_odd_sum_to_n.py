n = int(input("Digite um número inteiro: "))

soma_pares = 0
soma_impares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i


print(f"A soma de numeros PARES de 1 até {n} é {soma_pares}")
print(f"A soma de numeros IMPARES de 1 até {n} é {soma_impares}")
