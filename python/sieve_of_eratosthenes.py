def prime_sieve(max_num):
    list_of_nums  = range(max_num +1)
    for i in range(max_num + 1):
        if i == 0:  list_of_nums[i] = -1
        elif i == 1: list_of_nums[i] = -1
        else:
            for j in range(i + 1, max_num + 1):
                if list_of_nums[j] % i == 0:
                    list_of_nums[j] = -1
                else:
                    pass
    return list_of_nums
