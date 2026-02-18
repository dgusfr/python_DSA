array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
value = 11


def binary_search(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Verifica se o alvo está no meio
        if arr[mid] == targetVal:
            return mid

        # Se o alvo for maior, ignora a metade esquerda
        if arr[mid] < targetVal:
            left = mid + 1
        # Se o alvo for menor, ignora a metade direita
        else:
            right = mid - 1

    return -1


result = binary_search(array, value)

if result != -1:
    print(f"Found in index: {result}")
else:
    print("Value not found")
