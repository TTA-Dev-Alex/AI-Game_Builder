#step one, print your title
print("Guess the number!")

#step two, enter the number value here. Pick a number from 1 - 10
number = 5

#step three, ask the user to guess the number
guess = input("Your guess is: ")

#step four, writing the conditional statement to see if they guessed right or wrong

#explain the significance of adding int() to guess.

if int(guess) > number:
    print("Too high!")
if int(guess) < number:
    print("Too low!")
if int(guess) == number:
    print("That's right!")
