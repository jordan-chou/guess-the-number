#   Jordan Chou
#   Dec. 18, 2019
#   A number guessing game

from random import randint

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again\n")
            continue
        else:
            return userInput
            break

print("Welcome to Guess The Number game!\n")
attempts = 1
randomNum = randint (0, 20)

userInput = inputNumber("Guess a number between 0 and 20: ")

while userInput != randomNum:
    if userInput > 20 or userInput < 0:
        userInput = inputNumber("Your guess was out of range:\t")
    elif userInput > randomNum:
        userInput = inputNumber("Your guess is too high:\t")
    elif userInput < randomNum:
        userInput = inputNumber("Your guess is too low:\t")

    attempts += 1

print("\nCorrect! The number was " + str(randomNum))
if attempts == 1:
    print("You guessed in 1 attempt")
else:
    print("You guessed in " + str(attempts) + " attempts")
