import sys

while True:
 print("Is it raining outside?")
 response = input()
 if response == "no":
        print("You can go outside")
        print("Enjoy your walk!")
        sys.exit()

 if response == "yes":
     print("Do you have an umbrella?")
     response = input()

 if response not in ("yes", "no"):
    print("Please type 'yes' or 'no'")
    

    if response == "yes":
        print("You can go outside")
        print("Enjoy your walk!")
        sys.exit()
    elif response == "no":
        print("Wait until it clears up.")
        print("Is it still raining?")
        response = input()
        
    if response not in ("yes", "no"):
     print("Please type 'yes' or 'no'")
    
     if response == "no":
            print("You can go outside")
            print("Enjoy your walk!")
            sys.exit()
     else:
            continue