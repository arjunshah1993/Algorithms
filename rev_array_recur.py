arr = [3, 5, 2, 6, 2, 1]
i = len(arr) - 1


def arr_rev_recur(array, i):
    if i <= len(array)/2 - 1:
        return array
    temp = array[i]
    array[i] = array[len(array) - i - 1]
    array[len(array) - i - 1] = temp
    return arr_rev_recur(array, i - 1)


print(arr_rev_recur(arr, i))