import random
import sys



def answer(fortune):
    if fortune == 1:
     print("You are amazing")
    elif fortune == 2:
     print("Today is not a good day")
    elif fortune == 3:
     print("Enjoy the day")
    elif fortune == 4:
     print("You got this")
    elif fortune == 5:
     print("Look for the silver lining")
    elif fortune == 6:
     print("Take it slow today")
    elif fortune == 7:
     print("Gold is just around the corner")
    elif fortune == 8:
     print("Good things come to those who wait")
    
    return

while True:
 print("To get your fortune, type 'shake' or 'quit' to leave")

 response = input()

 while True:
  if response == "shake":
   print("Here is your fortune")
   answer(random.randint(1,8))
   sys.exit()
 
  if response == "quit":
   print("No fortune for you")
   sys.exit()

  elif response != "shake" or "quit":
   print("Try again")
   break
   

   
 
   


