'''
  Author: Diogo Costa
  003 - List Less Than Ten
  
  Description: README.md
'''

# Static list of numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Ask the user for a number in order to be used in filter function
lessThan = int(input('Insert a number: '))

# Doing the entire operation in one line 
print(list(filter(lambda x: x < lessThan, numbers)))