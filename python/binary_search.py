def binary_search(numbers, key):
    low = 0
    high = len(numbers) - 1
    while(low <= high):
        pivot = (low + high) / 2
        if numbers[pivot] == key:
            return pivot
        elif key < numbers[pivot] < key:
            high = pivot - 1
        else:
            low = pivot + 1
    return -1
