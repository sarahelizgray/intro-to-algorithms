def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[i]:
                swap = numbers[j]
                numbers[j] = numbers[i]
                numbers[i] = swap
    return numbers

result = bubble_sort([1, 2, 3, 4, 5, 23, 56, 78, 22, 45, 9])

print "result is " + str(result)