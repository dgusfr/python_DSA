array = [12, 8, 9, 3, 11, 5, 4]


def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)

        merge(arr, start, mid, end)

    return arr


def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]

    top_left, top_right = 0, 0

    for k in range(start, end):
        if top_left < len(left) and (
            top_right >= len(right) or left[top_left] <= right[top_right]
        ):
            arr[k] = left[top_left]
            top_left += 1
        else:
            arr[k] = right[top_right]
            top_right += 1


print(merge_sort(array))
