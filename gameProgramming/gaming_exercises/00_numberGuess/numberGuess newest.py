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
       +=================+
       |                 |
       |  darrrl mcnish  |
       |                 |
       |                 |
       |                 |
       +=================+

     """)


playerName = input("what should i call you?\nType your name and press enter.\n")
# VERIFY INPUT WHENEVER POSSIBLE!
print(f"you want me to call you {playerName}. Is that correct?")
isCorrect = input("please type yes if correct, no if not correct.\n")
if isCorrect == "yes":
    print(f"ok {playerName}, let's continue!")
else:
    playerName = input("what should i call you?\nType your name and press enter.\n")   

# CPU SECRET NUMBER GENERATION
secretNumber = random.randit(0, 20)
print(secretnumber)
 
# GAME LOOP
print("you need to guess a number from 0 to 20 and you have four guesses. \nIf you guess it right, you")

while playerScore != 3 and cpuScore != 3:
    # pass -- Tells python to skip this block of code.
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    numGuesses = 0
    for guesses in range(4) :
        print(f"you have {4 - numGuesses} guesses remaining.\n")
        playerGuess = int(input("type a number from 0 to 20 and push ENTER.\n"))
        # input() saves all data as a STRING by default
        # int() will convert to an INTERGER
        # float() will convert to a FLOAT
        print(f"you have chosen {playerGuess}. Let's see if you're right!\n")
        if playerGuess == secretNumber:
            print("woah dude, what a guess! you got it!/n")
            playerScore += 1
            break # IMMEDIATELY EXIT ANY LOOP YOU ARE IN!
        else:
            print("you did not guess correctly.\n")
            if playerGuess > secretNumber:
                print("your guess is too high.\n")
            else:
                print("you guess is too low.\n")
        numGuesses += 1
    if playerGuess != secretNumber:
        cpuScore += 1
        print("the CPU wins a point since you ran out of guesses.\n")
if playerScore >= 3:
    print("winner, winner chicken dinner! you scored 3 points first!\n")
else:
    print("yo, you lost to a computer. you are a scrub.\n")