# INSTRUCTIONS: Build a command-line based zombie fighting game.
# =========================================================================================================

# In this game, you and a zombie will each be given a certain amount of health. (Perhaps: You 70, Zombie 15).

# For each round, you will be asked to guess a random number between 1 and 5.
# If your guess matches the random number of the Zombie -- you inflict a random amount of damage between 1 and 5.
# If you guess does not match the random number of the Zombie -- the Zombie inflicts a random amount of damage to you between 1 and 5.
# Each round the zombie is given a new random number and you must guess again.

# The game ends when you or the zombie gets to 0 health.

# Note: You should use the inquirer module to take in user commands.

# ===========================================================================================================

# Load the inquirer, math and random modules
import inquirer, math, random

# Set initial health amounts.
userHealth = 70
zombieHealth = 15

# Created a generic function that checks if the user won or lost.
def checkRound():

  print("\n")

  # If the user has less than 0 health.... then the user lost.
  if userHealth <= 0:

    print("###############################################")
    print("")
    print("Game over dude. It looks like you're dead.")
    print("")
    print("###############################################")

    # Exit the game
    exit()

  # If the zombie has less than 0 health.... then the user won.
  if zombieHealth <= 0:

    print("###############################################")
    print("")
    print("Victory! You defeated the zombie and survived!")
    print("")
    print("###############################################")

    # Exit the game
    exit()

  # After performing the "check", the next round is initiated.
  playRound()

# Set initial health amounts.
userHealth = 70
zombieHealth = 15

# This function holds the game logic
def playRound():
    global userHealth, zombieHealth

    # We create a list prompt. Specifying that the user must pick a random number between 1 and 5.
    questions = [
        inquirer.List("userGuess",
            message="Try to stay alive! Guess a number between [1-5]",
            choices=["1", "2", "3", "4", "5"]
        )

    ]

    answers = inquirer.prompt(questions)

    # If the user is still alive or the zombie is still alive
    if userHealth > 0 or zombieHealth > 0:

        # Assign a random damage value for the round.
        damage = random.randint(1, 5)

        # The zombie should choose a random number.
        zombieNum = random.randint(1, 5)
        print("")
        print("")
        print("Zombie rolled " + str(zombieNum))

        # If the user's guess matches the number then...
        if zombieNum == int(answers['userGuess']):

            # Subtract the damage amount from the zombie's health.
            zombieHealth -= damage
            print("YOU HIT THE ZOMBIE WITH " + str(damage) + " damage")
            print("You have " + str(userHealth) + " health left. The Zombie has " + str(zombieHealth) + " health left.")

            # Check if the game is over.
            checkRound()

        else:
            # Subtract the damage amount from the user's health.
            userHealth -= damage
            print("OH NO! The zombie slashed you with " + str(damage) + " damage")
            print("You have " + str(userHealth) + " health left. The Zombie has " + str(zombieHealth) + " health left.")

            # Check if the game is over.
            checkRound()

# Starts the game!
playRound()