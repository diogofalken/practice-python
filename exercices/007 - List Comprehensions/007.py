'''
  Author: Diogo Costa
  007 - List Comprehensions
  
  Description: README.md
'''

# Given List 
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# One line of code to check the even numbers in a list
result = [x for x in a if x % 2 == 0]

print(result)