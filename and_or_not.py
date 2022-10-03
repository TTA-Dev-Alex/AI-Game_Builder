# create a list to enter items
bag = []
# give players a story and explain how to play the game
print("You stand over a bubbling Witches Cauldron. You sense that you need to put items into the mixture to create something incredible.")
print("You look around the room for 3 items to collect.")
print("You see...")
# enter number 1, 2, or 3 to select and item to put in your bag. 
item1 = input("1. Frog, 2. Blue Crystal, 3. Orange Powder")
if item1 == "1":
    bag.append("Frog")
    print("The Frog has been added to your bag")
if item1 == "2":
    bag.append("Blue Crystal")
    print("The Blue Crystal has been added to your bag")
if item1 == "3":
    bag.append("Orange Powder")
    print("The Orange Powder has been added to your bag")
print("You also see...")
item2 = input("1. A Dragonfly, 2. A Spider, 3. A butterfly")
if item2 == "1":
    bag.append("Dragonfly")
    print("The Dragonfly has been added to your bag")
if item2 == "2":
    bag.append("Spider")
    print("The Spider has been added to your bag")
if item2 == "3":
    bag.append("Butterfly")
    print("The Butterfly has been added to your bag")
print("You need one more item. You also see...")
item3 = input("1. Green Potion, 2. Blue Potion, 3. Red Potion")
if item3 == "1":
    bag.append("Green Potion")
    print("The Green Potion has been added to your bag")
if item3 == "2":
    bag.append("Blue Potion")
    print("The Blue Potion has been added to your bag")
if item3 == "3":
    bag.append("Red Potion")
    print("The Red Potion has been added to your bag")
print("Your bag is full. You have...")
for x in bag:
    print(x)
print("You add all your items to the cauldron and...")
# this is the section students should be focused on, with AND, OR and NOT statements.
# student should consider the implications of each statement here
if "Frog" in bag and "Dragonfly" in bag:
    print("The frog ate the dragonfly. What did you expect?")
    exit()
if "Blue Crystal" not in bag:
    print("The cauldron seems to be missing something, there is no magic here.")
    exit()
if "Green Potion" in bag or "Blue Potion" in bag:
    print("Out of the cauldron comes a ghost. Great, now your house is haunted.")
    exit()
else:
    print("You produce a powerful potion. Good work!")
