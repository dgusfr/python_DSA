n = int(input("Digite um número inteiro: "))

soma = 0

for i in range(1, n + 1):
    if i < n:
        print(f"{i} + ", end="")
    else:
        print(f"{i} = ", end="")
    soma += i

print(f"{soma}", end="")
