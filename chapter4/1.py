def sum(arr):
    total = 0
    for x in arr:
        total += x

    return total


print(sum([1, 2, 3, 4]))


def sum_recursion(list):
    if not list:
        return 0
    return list[0] + sum(list[1:])


print(sum_recursion([1, 2, 3, 4]))


def count(list):
    if not list:
        return 0
    return 1 + count(list[1:])


print(count([1, 3, 6, 4, 5, 3, 45, 6, 4, 3, 3, 4, 5, 6, 7]))
