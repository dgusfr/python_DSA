"""

Desenvolva um algoritmo que recebe um número inteiro (N) digitado pelo usuário e seja impresso na tela a soma de todos os números inteiros de 1 até N.

Exemplo: se o usuário digitar 7, o programa deverá exibir 1+2+3+4+5+6+7=28.


"""

n = int(input("Digite um número inteiro: "))

soma = 0

for i in range(1, n + 1):
    if i < n:
        print(f"{i} + ", end="")
    else:
        print(f"{i} = ", end="")
    soma += i

print(f"{soma}", end="")
