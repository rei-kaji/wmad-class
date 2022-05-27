# Write a Python function which receives 2 lists as its input parameters and checks whether one of the list is included in another input list. A list A is considered to be included in List B, if all elements in A are elements in B.

def compareLists(list1, list2):

    a = set(list1)
    b = set(list2)

    if a == b:
        print("Lists l1 and l3 are equal")
    else:
        print("Lists l1 and l3 are not equal")


compareLists([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
compareLists([1, 2, 3, 4, 5], [6, 7, 8, 9])
