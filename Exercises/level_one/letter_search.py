word = input("Digite uma palavra (até 250 caracteres): ")
letter = input("Digite uma letra: ")


def count_letter(word, letter):
    count = 0
    for char in word.lower():
        if char == letter.lower():
            count += 1
    return count


count = count_letter(word, letter)
print(f"A letra '{letter}' apareceu {count} vezes na palavra '{word}'.")
