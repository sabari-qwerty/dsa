array = [38, 27, 43, 10]


def marge(left, right):

    result = []

    i, j = 0, 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    result += left[i:]
    result += right[j:]

    return result


def margeSort(array):

    if len(array) <= 1:

        return array

    pivot = len(array) // 2

    left, right = margeSort(array[:pivot]), margeSort(array[pivot:])

    return marge(left, right)


print(margeSort(array))
