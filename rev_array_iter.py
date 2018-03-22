arr = [1, 2, 3, 4, 5]


def reverse_array(array):
    if len(array) % 2 == 0:
        half = int(len(array)/2)
        for i in range(0, half):
            temp = array[i]
            temp2 = array[len(array) - 1 - i]
            array[i] = temp2
            array[len(array) - 1 - i] = temp
    else:
        half = int(round(len(array)/2))
        for i in range(0, half):
            temp = array[i]
            temp2 = array[len(array) - 1 - i]
            array[i] = temp2
            array[len(array) - 1 - i] = temp
    return array


print(reverse_array(arr))
