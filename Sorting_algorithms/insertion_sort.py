array = [64, 34, 25, 12, 22, 11, 90, 5]


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        for j in range(j, -1, -1):
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort(array))
