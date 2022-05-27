# Problem1
# Implement a function which receives a list and returns True if the list is already sorted ascendingly and returns 0 if the list is not sorted ascendingly.

list1 = [1, 3, 2, 9, 6, 4, 3, 2, 5, 5]
list2 = [1, 2, 3, 4, 5, 6, -1]


def isAscendedSort(list):
    for i in range(len(list)):
        temp = list[i]
        for j in range(i+1, len(list)):
            if temp > list[j]:
                return 0
    return True


print(isAscendedSort(list1))
print(isAscendedSort(list2))
