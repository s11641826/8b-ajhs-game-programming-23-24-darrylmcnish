# select the secret number from a given range.
# player must guess that number.
# compare guess to the secret number.
# what happens if the guess is wrong?
    # tell them the guess is wrong.
    # Tell them the number of guesses left
    # Tell them if too High / Low.
# What happens if the guess is right?
    # Tell them the guess is correct.
    # Award a point.
# What happens of the player runs out of guesses?
    # Tell player round has been lost.
    # Award point to CPU.
# Check to see if player or CPU has >= 3 points, if so they win.

import random # Import the random module to ur code.

#DECLARATIONS
secretNumber = -1 
playerScore = 0
cpuScore = 0
numGuesses = 0
playerName = ""

print("""
       *~~~~~~~~~~~~~~~~~*
       |                 |
       |                 |
       |                 |
       |                 |

     """)



# CPU SECRET NUMBER GENERATION
secretNumber = random.randit(0, 20)
print(secretnumber)
 
# GAME LOOP
print("you need to guess a number from 0 to 20 and you have four guesses. \nIf you guess it right, you")

while playerScore != 3 or cpuScore != 3:
    # pass -- Tells python to skip this block of code.
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    for guesses in range(4) :
        print(f"you have {4 - numGuesses} guesses remaining.\n")
        playerGuess = input("type a number from 0 to 20 and push ENTER.\n")
        print(f"you have chosen {playerGuess}. Let's see if you're right! \n")