"""
Desenvolva um algoritmo que leia uma palavra e conte quantas vogais (a, e, i, o, u) existem em uma palavra. O algoritmo deve exibir o total de vogais encontradas.
"""


def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


word = input("Digite uma palavra: ")
vowel_count = count_vowels(word)
print(f"A palavra '{word}' contém {vowel_count} vogais.")
