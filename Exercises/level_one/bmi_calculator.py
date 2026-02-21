"""Desenvolva um algoritmo que recebe o valor da massa (em kg) e o valor da altura (em metros) de uma pessoa e retorne o valor do IMC (Índice de Massa Corporal), calculado pela seguinte expressão:"""

weight = float(input("Digite o peso em kg: "))
height = float(input("Digite a altura em metros: "))

imc = weight / (height**2)

if imc < 18.5:
    print(f"IMC: {imc:.2f} - Abaixo do peso")
elif 18.5 <= imc < 25:
    print(f"IMC: {imc:.2f} - Peso normal")
elif 25 <= imc < 30:
    print(f"IMC: {imc:.2f} - Sobrepeso")
else:
    print(f"IMC: {imc:.2f} - Obesidade")
