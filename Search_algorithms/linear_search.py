array = [3, 7, 2, 9, 5, 1, 8, 4, 6]
value = 42


def linear_search(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return None


result = linear_search(array, value)

if result != -1:
    print(f"Found in index: {result}")
else:
    print("Value not found in the array.")
