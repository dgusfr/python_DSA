word = input("Enter a word: ")


def is_palindrome(word):
    word = word.lower()
    inversed_word = ""

    for char in word:
        inversed_word = char + inversed_word

    for i in range(len(word)):
        if word[i] != inversed_word[i]:
            return False
    return True


if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is NOT a palindrome.")
