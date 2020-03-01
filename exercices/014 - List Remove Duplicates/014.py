'''
  Author: Diogo Costa
  014 - List Remove Duplicates
  
  Description: README.md
'''


# Version 1 using a loop and constructing a list
def removeDuplicatesV1(list):
    newList = []

    for cur in list:
        if cur in newList: continue
        newList.append(cur)

    return newList


# Version 2 using set function
def removeDuplicatesV2(list):
    return set(list)


if __name__ == "__main__":
    # Random List
    a = [1, 1, 1, 3, 4, 5]

    # Version 1 using a loop
    newList1 = removeDuplicatesV1(a)

    # Version 2 using a set() function
    newList2 = list(removeDuplicatesV2(a))

    # Print results
    print(f"Version 1: {newList1}")
    print(f"Version 2: {newList2}")