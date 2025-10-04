# this program says hello and asks for my name
import sys

print('Welcome to your first Adventure!')
print('What is your name, adventurer?') # ask for their name
myName = input() # get their name
print('It is good to meet you, ' + myName) # greet them
print("Are you ready to begin your adventure?") # ask if they are ready to begin
ready = input().lower() # get their answer
if ready == "yes":
    print("Let's begin!")
else: print("Too bad, you're going on an adventure anyway!")
while True:
   print('You are in a dark room. There is a door to your right and left. Which one do you take?') # ask which door they take
   door = input()  # get their answer
   if door == "left":
     print("You seen a treasure chest at the far end of the room but there is a sleeping dragon in front of it. Do you go past the dragon or go back?")
     leftDoor = input()
     if leftDoor == "go past the dragon" or leftDoor == "Go past the dragon" or leftDoor == "past the dragon" or leftDoor == "Past the dragon":
        print("The dragon wakes up and eats you! You lose!")
        sys.exit()
     elif leftDoor == "go back":
            print("You go back to the dark room.")
            continue
     else: print("You didn't choose a valid option. Please choose again.")
   elif door == "right":
    
     print("There is an old rickety bridge that looks like it could collapse at any moment. Do you cross the bridge or go back?")
     rightDoor = input()
     if rightDoor == "cross the bridge":
        print("You cross the bridge safely and find a room full of treasure! You win!")
        sys.exit()
     elif rightDoor == "go back" or rightDoor == "Go back" or rightDoor == "back" or rightDoor == "Back":
        print("You go back to the dark room. There is a door to your right and left. Which one do you take?")
        continue
     else: print("You didn't choose a valid option. Please choose again.")
   continue
   
