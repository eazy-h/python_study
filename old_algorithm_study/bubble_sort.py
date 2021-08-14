def bubble_sort(list):
    unsorted_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_index):
            if list[i] > list[i + 1]:
                sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]
        unsorted_index = unsorted_index - 1


list = [75, 23, 45, 1, 33, 96, 54, 12]
bubble_sort(list)

print(list)
