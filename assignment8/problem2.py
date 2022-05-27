#Problem2
#Write a function which receives a list and returns True if the list is “Partially sorted” 
# and returns False if the list is not “Partially Sorted”. A list is “Partially sorted” 
# if and only if there exists an item in the list which if removed, the list will become a sorted list. 
# For instance the following list is “Partially sorted”:[1,2,5,10,6,8,9] 
# This is partially sorted because it is not originally sorted but if we remove 10 from the list, then the list is sorted.


list1 = [1,3,2,9,6,4,3,2,5,5]
list2 = [1,2,3,4,5,6,-1]

def isAscendedSort(list):
  partiallyNumber = 0

  i = 0
  j = 1
  
  while i != int(len(list)):
    temp = list[i]
    i = i+1
    while j != int(len(list)):
      j = j+1
      if temp > list[j-1]:
        partiallyNumber = partiallyNumber +1
  
  
  if partiallyNumber == 1:
    return print("It's PartiallyList")
  else:
    return print("It's not PartiallyList")
      

print(isAscendedSort(list1))
print(isAscendedSort(list2))