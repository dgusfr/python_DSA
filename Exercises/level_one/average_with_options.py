exit = True

while exit:
    calculate = input("Enter 'w' for weighted or 'h' for harmonic or 'e' for exit: ")
    if calculate == "e":
        exit = False
        break
    if calculate == "w":
        grade1 = float(input("Enter the first grade: "))
        weight1 = float(input("Enter the weight for the first grade: "))
        grade2 = float(input("Enter the second grade: "))
        weight2 = float(input("Enter the weight for the second grade: "))
        grade3 = float(input("Enter the third grade: "))
        weight3 = float(input("Enter the weight for the third grade: "))

        weighted_average = (grade1 * weight1 + grade2 * weight2 + grade3 * weight3) / (
            weight1 + weight2 + weight3
        )
        print(f"The weighted average is: {weighted_average}")

    elif calculate == "h":
        grade1 = float(input("Enter the first grade: "))
        grade2 = float(input("Enter the second grade: "))
        grade3 = float(input("Enter the third grade: "))

        harmonic_average = 3 / (1 / grade1 + 1 / grade2 + 1 / grade3)
        print(f"The harmonic average is: {harmonic_average}")

    else:
        print("Invalid option. Please enter 'w' for weighted or 'h' for harmonic.")
