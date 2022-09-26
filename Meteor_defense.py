# Introduction
print("You are working at Space Forces Meteor Defense Station. Your job is to locate and intercept meteors before they"
      "\nreach earth. Upon detecting an incoming meteor, you will have 3 attempts to shoot it down. Guess coordinates "
      "\nbetween 1 - 5 to attempt to locate the meteor. Good luck!")

# create a list of meteor positions
meteors = [4, 5, 3, 2]
# create a score variable to keep track of the players progress
score = 0

# use a for loop to have the game loop through each meteor in the list
for x in meteors:
    # prompt the user and give them 3 missiles
    print("!!!ALERT: METEOR INCOMING!!!")
    missiles = 3
    # write a while loop that continues as long as the player has missiles
    while missiles > 0:
        # use knowledge from previous lessons to take user input (L1)
        # and compare it to the variable with IF statements (L2)
        guess = input("Enter the meteor coordinate: ")
        if int(guess) > x:
            print("Miss: Guess too high")
            missiles = missiles - 1
        if int(guess) < x:
            print("Miss: Guess too low")
            missiles = missiles - 1
        if int(guess) == x:
            print("Hit: Meteor Destroyed")
            # add to the score if the user guesses correctly
            score = score + 1
            # explain that break is used here in order to begin the next for loop
            break

# now that the for loop has been completed, we can use if statements to count the points and give the player an outcome.
if score == 0:
    print("You have failed, the earth is destroyed.")

if score == 1:
    print("Earth is heavily damaged, how will we ever rebuild?")

if score == 2:
    print("Earth is partially damaged, many lives have been lost.")

if score == 3:
    print("Earth was only slightly damaged, good work!")

if score == 4:
    print("Thanks to you, earth was untouched. All nations regard you as a hero.")
