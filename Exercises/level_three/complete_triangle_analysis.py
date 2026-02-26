import math


side_a = float(input("Digite a medida do primeiro lado do triângulo: "))
side_b = float(input("Digite a medida do segundo lado do triângulo: "))
side_c = float(input("Digite a medida do terceiro lado do triângulo: "))


def triangle_analysis(a, b, c):
    # Verificar existência do triângulo
    if a + b <= c or a + c <= b or b + c <= a:
        print(
            "Os valores informados não satisfazem a condição de existência de um triângulo."
        )
        return

    # Classificação por lados
    if a == b == c:
        print("O triângulo é equilátero.")
    elif a == b or a == c or b == c:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")

    # Classificação por ângulos
    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("O triângulo é também retângulo.")
    elif sides[0] ** 2 + sides[1] ** 2 < sides[2] ** 2:
        print("O triângulo é também obtusângulo.")
    else:
        print("O triângulo é também acutângulo.")

    # Perímetro
    perimeter = a + b + c
    print(f"O perímetro do triângulo é: {perimeter}")

    # Área usando fórmula de Heron
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"A área do triângulo é: {area}")

    # Cálculo dos ângulos usando a lei dos cossenos
    angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_c = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))

    print(f"Os ângulos internos do triângulo são:")
    print(f"Entre os lados {b} e {c}: {angle_a:.2f} graus")
    print(f"Entre os lados {a} e {c}: {angle_b:.2f} graus")
    print(f"Entre os lados {a} e {b}: {angle_c:.2f} graus")


triangle_analysis(side_a, side_b, side_c)
