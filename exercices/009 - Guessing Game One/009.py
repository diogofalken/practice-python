'''
  Author: Diogo Costa
  009 - Guessing Game One
  
  Description: README.md
'''

import random


def handleGuess(guess, randomNumber):
    # By Default you win guess == randomNumber
    val = 0

    if int(guess) > randomNumber:
        val = 1
    elif int(guess) < randomNumber:
        val = -1
    return val


def handleMessage(index):
    if index == 0:
        print("Your guess is right")
    elif index == 1:
        print("Your guess is too high")
    else:
        print("Your guess is too low")


if __name__ == '__main__':
    # Get random number
    randomNumber = random.randint(1, 9)

    run = True
    tries = 0

    # Main cycle
    while(run):
        guess = input('What is your guess: ')

        if guess == 'exit':
            print(f"END GAME, you had {tries} tries")
            run = False
        else:
            # Check if he guessed too low, too high, or exactly right
            response = handleGuess(guess, randomNumber)

            # Show the correct guess message
            handleMessage(response)

            # Increment tries
            tries += 1
