while True:
    name = input("Who are you?\n")
    attempts = 2
    while name != "Joe":
        print("I don't know you. You have " + str(attempts) + " attempts left. Try again.")
        name = input("Who are you?\n")
        attempts = attempts - 1
        if attempts == 0:
            print("I don't know you anymore. Go home!")
            exit()
    if name == "Joe":
        break

while True:
    password = input("Hello, Joe. What is the password? (It is a fish.)\n")
    attempts = 2
    while password != "swordfish":
        print("Incorrect password. Try again.")
        password = input("What is the password? (It is a fish.)" + "You have " + str(attempts) + " attempts left.\n")
        attempts = attempts - 1
        if attempts == 0:
            print("No more attempts left. Access denied.")
            exit()
    if password == "swordfish":
        break
print("Access granted.")
   
