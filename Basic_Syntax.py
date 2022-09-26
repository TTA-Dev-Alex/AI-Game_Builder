# This is an example of a comment, using the # symbol

# this is an example of a print statement
print("Hello world")

# this is an example of how we can take input from a user
answer = input("What is your name?")

# this is how we can concat variables and strings
print("nice to meet you " + answer + "!")

# this is an example of a variable
number = 5

# this is an example of an array, or a list of values held in one varialable statement
numbers = [1, 2, 3, 4, 5]

# this is a for loop, it will go through each value in an array
# i is an arbitrary placeholder, you can use any character/word here
for i in numbers:
  #this will loop through and print out each value in the given array
  print(i)
  
# this is a while loop, it runs as long as the condition is true
while number > 0:
  print("the loop is running")
  number = number - 1
  #since the number = 5, this loop will run 5 times

# this is an example of a forever loop, since the condition is literally true, it will always run  
while true:
  print("forever")
  # a loop can be stopped by writing break
  break
  # with a break statement, this loop will only run once
  
# this is an if statement
if number > 3:
    print("The number is bigger than 3")
if number < 3:
    print("The number is smaller than 3")
if number == 3:
    print("The number is 3")

    
