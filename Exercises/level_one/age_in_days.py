"""
Desenvolva um algoritmo que leia a data de nascimento de uma pessoa (dia, mês e ano) e a data atual (dia, mês e ano). O algoritmo deve calcular a idade dessa pessoa em dias e quantos anos ela tem com base na data atual. Considere que um ano tem 365 dias e um mês tem 30 dias para simplificar os cálculos.
"""

age = input("Digite sua data de nascimento: (dd/mm/aaaa): ")
current_date = input("Digite a data atual: (dd/mm/aaaa): ")


def calculate_age_in_days(age, current_date):
    age_day, age_month, age_year = age.split("/")
    current_day, current_month, current_year = current_date.split("/")

    birth_day, birth_month, birth_year = int(age_day), int(age_month), int(age_year)
    current_day, current_month, current_year = (
        int(current_day),
        int(current_month),
        int(current_year),
    )

    age_in_days = (
        (current_year - birth_year) * 365
        + (current_month - birth_month) * 30
        + (current_day - birth_day)
    )

    if current_month > birth_month and current_day > birth_day:
        age_in_years = current_year - birth_year
    else:
        age_in_years = current_year - birth_year - 1
    return age_in_days, age_in_years


print(calculate_age_in_days(age, current_date))
