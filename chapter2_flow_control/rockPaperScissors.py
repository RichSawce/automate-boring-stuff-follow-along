import random
import sys
print("Welcome to Rock, Paper, Scissors!")

Wins = 0
Losses = 0
Ties = 0
while True:
 choice = random.randint(0,2)
 cpuChoice = choice

 if choice == 0:
    cpuChoice = 'rock'
 if choice == 1:
    cpuChoice = 'paper'
 if choice == 2:
    cpuChoice = 'scissors'
    
 while True:
  playerChoice = input("Choose rock, paper, or scissors. Type 'quit' to exit the game.\n")
  if playerChoice == 'paper' and cpuChoice == 'rock':
     print("The computer chose " + cpuChoice)
     print("Paper covers Rock! You win!")
     Wins +=1
     print((str(Wins))+ " Wins," + (str(Losses)) + " Losses," + (str(Ties)) + " Ties")
     break
  elif playerChoice == 'paper' and cpuChoice == 'paper':
     print("The computer chose " + cpuChoice)
     print("It's a tie!")
     Ties +=1
     print((str(Wins))+ " Wins," + (str(Losses)) + " Losses," + (str(Ties)) + " Ties")
     break
  elif playerChoice == 'paper' and cpuChoice == 'scissors':
     print("The computer chose " + cpuChoice)
     print("Scissors cuts paper! You lose!")
     Losses +=1
     print((str(Wins))+ " Wins," + (str(Losses)) + " Losses," + (str(Ties)) + " Ties")
     break
  elif playerChoice == 'scissors' and cpuChoice == 'rock':
     print("The computer chose " + cpuChoice)
     print("Rock smashes scissors! You lose!")
     Losses +=1
     print((str(Wins))+ " Wins," + (str(Losses)) + " Losses," + (str(Ties)) + " Ties")
     break
  elif playerChoice == 'scissors' and cpuChoice == 'paper':
     print("The computer chose " + cpuChoice)
     print("Scissors cuts paper! You win!")
     Wins +=1
     print((str(Wins))+ " Wins," + (str(Losses)) + " Losses," + (str(Ties)) + " Ties")
     break
  elif playerChoice == 'scissors' and cpuChoice == 'scissors':
     print("The computer chose " + cpuChoice)
     print("It's a tie!")
     Ties +=1
     print((str(Wins))+ " Wins," + (str(Losses)) + " Losses," + (str(Ties)) + " Ties")
     break
  elif playerChoice == 'rock' and cpuChoice == 'rock':
     print("The computer chose " + cpuChoice)
     print("It's a tie!")
     Ties +=1
     print((str(Wins))+ " Wins," + (str(Losses)) + " Losses," + (str(Ties)) + " Ties")
     break
  elif playerChoice == 'rock' and cpuChoice == 'paper':
     print("The computer chose " + cpuChoice)
     print("Paper cover's rock! You lose!")
     Losses +=1
     print((str(Wins))+ " Wins," + (str(Losses)) + " Losses," + (str(Ties)) + " Ties")
     break
  elif playerChoice == 'rock' and cpuChoice == 'scissors':
     print("The computer chose " + cpuChoice)
     print("Rock smashes scissors! You win")
     Wins +=1
     print((str(Wins))+ " Wins," + (str(Losses)) + " Losses," + (str(Ties)) + " Ties")
     break
  elif playerChoice == 'quit':
        print("Goodbye!")
        sys.exit()
  elif playerChoice != 'rock' or 'paper' or 'scissors' or 'quit':
     print("Invalid choice, please choose again.\n")
     continue
  

    