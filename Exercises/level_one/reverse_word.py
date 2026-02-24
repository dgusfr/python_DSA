word = input("Digite uma palavra (até 250 caracteres): ")


def reverse_word(word):
    reversed_str = ""

    for i in range(len(word) - 1, -1, -1):
        reversed_str += word[i]

    return reversed_str


print(reverse_word(word))

"""
def reverse_word(word):
    return word[::-1]

print(reverse_word(word))
"""
