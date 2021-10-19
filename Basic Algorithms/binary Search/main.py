# binary search algorithm implementation with recursive and non-recursive methods.

def binary_search_recursive(array, x, start, finish):

    middle = (start + finish)//2

    if start > finish:
        return -1
    elif x == array[middle]:
        return middle
    elif x < array[middle]:
        return binary_search_recursive(array, x, start, middle-1)
    else:
        return binary_search_recursive(array, x, middle+1, finish)


def binary_search_iterative(array, x):
    start = 0
    finish = len(array) - 1

    while True:
        middle = (start + finish)//2

        if x == array[middle]:
            return middle
        elif x < array[middle]:
            finish = middle - 1
        elif x > array[middle]:
            start = middle + 1
        else:
            return -1


def main():
    my_list = [i*i for i in range(10)]
    print(binary_search_recursive(my_list, 9, 0, len(my_list) - 1))
    print(binary_search_iterative(my_list, 9))


main()
