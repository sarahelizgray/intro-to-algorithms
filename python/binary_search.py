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

result = binary_search([1,2,3,4,5,23,56,78], 23)

print "result is " + str(result)