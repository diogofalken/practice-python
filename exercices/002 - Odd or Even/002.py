'''
  Author: Diogo Costa
  002 - Odd or Even
  
  Description: README.md
'''

# Function to check if a given number is multiple of 4
def isMultipleOf4(number):
  if ((number & 3) == 0):
    return True
  return False

# Function to check the parity of a number
def checkParity(number):
  if (number % 2) == 0:
    return True # Given number is even
  return False # Given Number is odd

# Function to check if two given number divide evenly number / check
def checkDivision(number, check):
  if (number % check) == 0:
    return True
  return False

if __name__ == "__main__": 
  # Ask the user for a number
  number = int(input('Enter a random number: '))

  # Check if the number is even
  if checkParity(number) == True:
    if isMultipleOf4(number) == True:
      print(f"Number {number} is even and multiple of 4.")    
    else:
      print(f"Number {number} is even.")
  else:
      print(f"Number {number} is odd.")

  # Ask the user for a number
  check = int(input(f"Now enter a value to divide {number}: "))

  # Checks if the division of number and check divides evenly
  if checkDivision(number, check) == True:
      print(f"{number}/{check} divides evenly.")
  else:
      print(f"{number}/{check} does not divides evenly.")

    


