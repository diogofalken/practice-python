'''
  Author: Diogo Costa
  004 - Divisors
  
  Description: README.md
'''

# Check if is diviser of a number
def isDiviser(number, diviser):
  return number % diviser == 0

# Ask user for a number
number = int(input('Enter a number: '))

listRange = range(1, number + 1)

result = []

for x in listRange:
  if isDiviser(number, x) == True:
    result.append(x)

print(result)