array = [2, 4, 6, 8, 10,  12,   14, 16, 18, 20]
target = 10


def binarySearch(array, target):
    low = 0
    high = len(array) -1

    while low <= high:

        center = low + (high - low) // 2


        if array[center] == target:

            return array[center]
        
        elif array[center] < target:

            low += 1

        else:
            high -= 1

    return -1


        


print(binarySearch(array, target))