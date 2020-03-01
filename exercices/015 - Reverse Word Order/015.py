'''
  Author: Diogo Costa
  015 - Reverse Word Order
  
  Description: README.md
'''


def invertString(string):
    # Split by spaces the user string
    invertedString = string.split()

    # Now change the order of the string with [::-1] operator
    invertedString = invertedString[::-1]

    # Now join the entire string and put back the spaces
    invertedString = " ".join(invertedString)

    return invertedString


if __name__ == "__main__":
    print("------ Reverse Word Order ------")
    userValue = input("Insert a long string container multiple words: ")

    # Call the function to invert string and assign the returned value
    invertedString = invertString(userValue)

    # Print the final result
    print(invertedString)
