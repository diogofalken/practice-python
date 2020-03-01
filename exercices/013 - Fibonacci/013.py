'''
  Author: Diogo Costa
  013 - Fibonacci
  
  Description: README.md
'''


def generateFibonacci(nValues):
    # By Default numbers[0] = 0 and numbers[1] = 1
    numbers = [0, 1]

    for cur in range(2, nValues):
        prevValue = numbers[cur - 1]  # Get n - 1 value
        prevPrevValue = numbers[cur - 2]  # Get n - 2 value

        # Add the number to the list
        numbers.append(prevValue + prevPrevValue)

    return numbers


if __name__ == "__main__":
    print("------ Fibonacci Sequence ------")
    nValues = int(
        input("Enter how many numbers from Fibonnaci sequence to generate: "))

    # Get the Fibonacci List with n values
    fibonacciList = generateFibonacci(nValues)

    print(fibonacciList)
