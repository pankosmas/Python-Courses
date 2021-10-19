# Insertion sort algorithm *Swap values a,b = b,a*
# It works for all data types (primitive) floats, ints, strings etc.

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:                            # with > for descending sorting
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break


def main():
    array = [9, 2, 4, 7, 1, 8, 6, 3]
    insertion_sort(array)
    print(array)


main()
