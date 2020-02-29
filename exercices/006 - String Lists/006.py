'''
  Author: Diogo Costa
  006 - String Lists
  
  Description: README.md
'''

# Ask for a string
value = input('Insert a word: ')

# Check if the value is a palindrome
if value == value[::-1]:
  print(f"{value} is a palindrome.")
else:
  print(f"{value} isn't a palindrome.")
