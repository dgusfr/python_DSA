"""
Crie um algoritmo que leia três valores correspondentes aos lados de um triângulo, verifique se os valores formam um triângulo válido, em caso positivo, classifique ele em equilátero, isósceles ou escaleno.
"""


def classify_triangle(side1, side2, side3):
    # Verificar se os lados formam um triângulo válido
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        if side1 == side2 == side3:
            return "Equilátero"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Não é um triângulo válido"


# Exemplo de uso
side1 = float(input("Digite o primeiro lado do triângulo: "))
side2 = float(input("Digite o segundo lado do triângulo: "))
side3 = float(input("Digite o terceiro lado do triângulo: "))

print(classify_triangle(side1, side2, side3))
