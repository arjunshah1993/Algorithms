import numpy as np
arr = np.array([1,1,2,2,3,3])


def arr_sorted(array):
    for i in range(0, len(array)-1):
        if array[i] > array[i+1]:
            return "Not sorted"
        else:
            return "Sorted"


print(arr_sorted(arr))