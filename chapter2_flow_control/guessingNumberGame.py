import random
import sys
print("Welcome to the Guess the Number Game!")
done = False
difficulty = input(
    "Choose a difficulty. Type 'easy' 'medium' or 'hard':\n").lower()
while True:
 if difficulty == "easy":
    number = random.randint(1, 10)
 elif difficulty == "medium":
    number = random.randint(1, 100)
 elif difficulty == "hard":
    number = random.randint(1, 1000)
 else:
    print("Please choose a valid difficulty")
    difficulty = input(
        "Choose a difficulty. Type 'easy' 'medium' or 'hard':\n").lower()
    continue
 if difficulty == "easy":
  print("I'm thinking of a number between 1 and 10")
 if difficulty == "medium":
  print("I'm thinking of a number between 1 and 100")
 if difficulty == "hard":
  print("I'm thinking of a number between 1 and 1000")
 track = 0
 while True:
    guess = input("Take a guess.\n")
    track +=1
    if guess == "" or not guess.isdigit() and difficulty == "easy":
         print("Please enter a number between 1 and 10")
         continue
    elif guess == "" or not guess.isdigit() and difficulty == "medium":
         print("Please enter a number between 1 and 100")
         continue
    elif guess == "" or not guess.isdigit() and difficulty == "hard":
         print("Please enter a number between 1 and 1000")
         continue
    guess = int(guess)

    if guess < number:
          print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Good job! You guessed my number in " + str(track) + " tries!")
         
        print("Would you like to play again? (yes or no)")
        while True:
            answer = input().lower()
            if answer == "yes":
                difficulty = 0
                track = 0
                done = True
                break
            elif answer == "no":
                print("Goodbye!")
                sys.exit()
            elif answer != "yes" and answer != "no":
                print("Please answer with 'yes' or 'no'.")
                continue
            break
        if done:
            break
        
