array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
value = 11


def binary_search(arr, targetVal, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == targetVal:
            return mid
        if targetVal < arr[mid]:
            return binary_search(arr, targetVal, left, mid - 1)
        else:
            return binary_search(arr, targetVal, mid + 1, right)
    return None


result = binary_search(array, value)
print(f"Index of {value} in the array: {result}")
