cpf = input("Digite os nove primeiros números do CPF (sem pontos ou traços): ")
cpf_numbers = []

try:
    numbers = int(cpf)
    cpf_numbers.append(numbers)
    print(f"List after adding number: {cpf_numbers}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")


def calculate_cpf_digits(cpf_numbers):
    v1 = 0
    v2 = 0

    for i in range(0, len(cpf_numbers)):
        for j in range(10, 1, -1):
            v1 = v1 + (cpf_numbers[i] * j)

    if v1 % 11 < 2:
        v10 = 0
    else:
        v10 = 11 - (v1 % 11)

    for i in range(0, len(cpf_numbers)):
        for j in range(11, 1, -1):
            v2 = v2 + (cpf_numbers[i] * j)

    if v2 % 11 < 2:
        v11 = 0
    else:
        v11 = 11 - (v2 % 11)

    print(f"First verification digit: {v10}")
    print(f"Second verification digit: {v11}")


calculate_cpf_digits(cpf_numbers)
