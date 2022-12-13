def compare(arr1, arr2):
    # The odd return values for this function allow for easier sorting in pt2
    num_elem = min(len(arr1), len(arr2))
    for i in range(num_elem):
        left = arr1[i]
        right = arr2[i]
        if type(left) == type(right) == int:
            if left < right:
                return -1
            if left > right:
                return 1
        elif type(left) == type(right) == list:
            result = compare(left, right)
            if result != 0:
                return result
        else:
            if type(left) == int:
                result = compare([left], right)
            else:
                result = compare(left, [right])
            if result != 0:
                return result
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1

    return 0
