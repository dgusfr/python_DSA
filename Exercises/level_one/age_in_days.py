age = input("Digite sua data de nascimento: (dd/mm/aaaa): ")
current_date = input("Digite a data atual: (dd/mm/aaaa): ")


def calculate_age_in_days(age, current_date):
    birth_day, birth_month, birth_year = age.split("/")
    current_day, current_month, current_year = current_date.split("/")

    birth_day, birth_month, birth_year = (
        int(birth_day),
        int(birth_month),
        int(birth_year),
    )
    current_day, current_month, current_year = (
        int(current_day),
        int(current_month),
        int(current_year),
    )

    total_dias_nascimento = (birth_year * 365) + (birth_month * 30) + birth_day
    total_dias_atual = (current_year * 365) + (current_month * 30) + current_day

    age_in_days = total_dias_atual - total_dias_nascimento

    age_in_years = 0
    if current_year > birth_year:
        age_in_years = current_year - birth_year
        if current_month < birth_month:
            age_in_years -= 1
        elif current_month == birth_month and current_day < birth_day:
            age_in_years -= 1

    return age_in_days, age_in_years


print(calculate_age_in_days(age, current_date))
