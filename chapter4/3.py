from time import sleep


def print_items2(list):
    for item in list:
        sleep(1)
        print(item)


print_items2([2, 6, 4, 8, 10])
