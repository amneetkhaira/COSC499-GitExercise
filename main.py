import random
#Generate a random number between 1 and 25
randomNumber = random.randint(1,25)

#Ask user to enter a number
print('Guess the number between 1 and 25')
#Assign user input to a variable
guess = input()
userGuess = int(guess)

# Compare random number with user's guess.
if guess == randomNumber:
    print('That is the correct guess!')
if guess != randomNumber:
    print("Sorry that is incorrect. The number was " + str(randomNumber))
#Simple change 