arr = [1, 2, 3, 4]


def arr_sorted_recur(array):
    if len(array) == 0 or len(array) == 1:
        return True

    return array[0] <= array[1] and arr_sorted_recur(array[1:])


if arr_sorted_recur(arr):
    print("Sorted")
else:
    print("Not sorted")