'''
  Author: Diogo Costa
  001 - Character Input
  
  Description: README.md
'''

name = input('What is your name: ')

age = int(input('What is your age: '))

nMessages = int(input('How many times do you want to see the message: '))

year = abs(100 - int(age)) + 2020
answer = f"Hello {name}, you will be 100 years old in {year}."

for i in range(nMessages):
  print(f"{answer}")