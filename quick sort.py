array = [4, 9, 5, 8, 1, 10, 6, 7]


#  first solution

# for i in range(0, len(array)):

#     for j in range(i, len(array)):

#         if array[i] > array[j]:

#             array[i], array[j] = array[j], array[i]






#  second solution


def quickSort(array):

    if len(array) <= 1:

        return array

    pivot = array[len(array) // 2]

    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quickSort(left) + middle + quickSort(right)


print(quickSort(array))
