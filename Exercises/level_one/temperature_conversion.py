celsius = float(input("Digite a temperatura em Celsius (°C): "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15
reaumur = celsius * 4 / 5
rankine = (celsius + 273.15) * 9 / 5
speed_of_sound = 331.3 * (1 + (celsius / 273.15)) ** 0.5

print(f"A temperatura {celsius}°C é equivalente a:")
print(f"Fahrenheit: {fahrenheit}°F")
print(f"Kelvin: {kelvin}K")
print(f"Reaumur: {reaumur}°Re")
print(f"Rankine: {rankine}°Ra")
print(f"Velocidade do som: {speed_of_sound:.2f} m/s")
