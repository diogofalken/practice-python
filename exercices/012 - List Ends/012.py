'''
  Author: Diogo Costa
  012 - List Ends
  
  Description: README.md
'''


def handleList(list):
    return [
        x for x in list if list.index(x) == 0 or list.index(x) == (len(a) - 1)
    ]


if __name__ == "__main__":
    # Random list of numbers
    a = [5, 10, 15, 20, 25]

    # Get the list with just the first and last element of list a
    finalList = handleList(a)

    # Show the final list
    print(finalList)
