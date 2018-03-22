arr = [1, 2, 3, 4]


def arr_sorted(array):
    flag = False
    for i in range(0, len(array) - 1):
        if array[i] > array[i + 1]:
            flag = True
    if flag:
        return "Not sorted"
    return "Sorted"


print(arr_sorted(arr))
