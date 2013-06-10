def sequential_search(numbers, key):
    for index in range(len(numbers)):
        if numbers[index] == key:
            return index #There it is!
    return -1 #Nope, not in the array


result = sequential_search([1,2,3,4,5,23,56,78], 23)

print "result is " + str(result)