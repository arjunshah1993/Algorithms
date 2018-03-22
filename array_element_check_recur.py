arr = [0, 4]
ele = 4


def array_element_checker(array, element):
    if len(array) == 0:
        return False
    elif len(array) == 1:
        if array[0] == element:
            return True
    else:
        return array[0] == element or array_element_checker(array[1:], element)


if array_element_checker(arr, ele):
    print("Yes")
else:
    print("No")

