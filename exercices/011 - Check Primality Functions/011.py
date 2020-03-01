'''
  Author: Diogo Costa
  011 - Check Primality Functions
  
  Description: README.md
'''


# Check if a given number is prime or not
def checkPrime(num):
    maxNumber = int(num / 2) + 1

    for i in range(2, maxNumber):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("------- Check Primality Functions -------")
    userInput = int(input("Insert a number: "))

    if checkPrime(userInput) == True:
        print(f"{userInput} is a prime number.")
    else:
        print(f"{userInput} is a not prime number.")
