def find_index(numbers, key):
    for index in range(len(numbers)):
        if numbers[index] == key:
            return index #There it is!
    return -1 #Nope, not in the array