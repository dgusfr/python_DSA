salary = float(input("Digite o salário bruto: "))


def net_salary(salary):
    inss = salary * 0.11
    fgts = salary * 0.08
    ir = salary * 0.05

    net_salary = salary - inss - fgts - ir
    return net_salary


print(f"O salário líquido é: {net_salary(salary):.2f}")
