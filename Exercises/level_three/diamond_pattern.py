"""

Desenvolva um algoritmo em que o usuário digite um número inteiro ímpar positivo (N) e seja impresso na tela um “diamante”, conforme o exemplo abaixo para N=9 (nove linhas, nove colunas e nove asteriscos na linha central). Caso o usuário digite um número negativo ou par, o programa deverá imprimir uma mensagem de erro para o usuário.
“Diamante” para N=9
"""

number = int(input("Digite um número inteiro ímpar positivo: "))


def diamond_pattern(n):
    if n <= 0 or n % 2 == 0:
        print("Erro: O número deve ser um inteiro ímpar positivo.")
        return

    middle = n // 2
    for i in range(n):
        distance = middle - i
        if distance < 0:
            distance = -distance

        spaces = distance
        stars = n - 2 * spaces
        line = (" " * spaces) + ("*" * stars)
        print(line)


diamond_pattern(number)
