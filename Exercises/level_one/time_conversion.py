"""
Escreva um algoritmo que converta um determinado período expresso em dias, horas, minutos e segundos para apenas segundos.
"""

days = int(input("Digite o número de dias: "))
hours = int(input("Digite o número de horas: "))
minutes = int(input("Digite o número de minutos: "))
seconds = int(input("Digite o número de segundos: "))


def time_conversion(days, hours, minutes, seconds):
    total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
    return total_seconds


print(time_conversion(days, hours, minutes, seconds))
