import math


def binary_search(list_data, item):
    low = 0
    high = len(list_data) - 1
    while low <= high:
        mid = math.ceil((low + high) / 2)
        guess = list_data[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 9))
print(math.log(100, 2))
