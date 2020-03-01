'''
  Author: Diogo Costa
  008 - Rock Paper Scissors
  
  Description: README.md
'''

# Check if the player wants to reset the game
def resetGame():
  val = int(input('Wanna play again(0 - NO, 1 - YES): '))
  if val == 0:
    return False
  return True

# Check Rock Rule
def checkRock(p1, p2):
  if p1 == 1 and p2 == 2 or p1 == 2 and p2 == 1:
    return True
  return False

# Check Scissors Rule
def checkScissors(p1, p2):
  if p1 == 2 and p2 == 3 or p1 == 3 and p2 == 2:
    return True
  return False

# Check Paper Rule
def checkPaper(p1, p2):
  if p1 == 3 and p2 == 1 or p1 == 1 and p2 == 3:
    return True
  return False

# Handle Messages
def handleMessages(player1, player2, winningPlay):
  if player1 == winningPlay:
      print("PLAYER 1 WINS") 
  elif player2 == winningPlay:
    print("PLAYER 2 WINS") 
  else:
    print("DRAW")

if __name__ == '__main__':
  run = True
  while(run): 
    print("--------------- Rock Paper Scissors ---------------")
    print("----|| Rock - 1 || Scissors - 2 || Paper - 3 ||----" )

    # Ask for the plays
    player1 = int(input("Player one: "))
    player2 = int(input("Player two: "))

    # By default it's a draw
    winningPlay = 0;

    if checkRock(player1, player2) == True: # If one of the players won with rock
      winningPlay = 1
    elif checkScissors(player1, player2) == True: # If one of the players won with scissors
      winningPlay = 2
    elif checkPaper(player1, player2) == True: # If one of the players won with paper
      winningPlay = 3

    # Emit message, win lose or draw
    handleMessages(player1, player2, winningPlay)
  
    # Check if the player wants to reset or stop the game
    run = resetGame()