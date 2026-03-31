#Tic Tac Toe Game
import random
import sys

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

win = [['top-L', 'top-M', 'top-R'],
       ['mid-L', 'mid-M', 'mid-R'],
       ['low-L', 'low-M', 'low-R'],
       ['top-L', 'mid-L', 'low-L'],
       ['top-M', 'mid-M', 'low-M'],
       ['top-R', 'mid-R', 'low-R'],
       ['top-L', 'mid-M', 'low-R'],
       ['top-R', 'mid-M', 'low-L']]




def printBoard():
 print(board['top-L']+ '|' + board['top-M'] + '|' + board['top-R'])
 print('-+-+-')
 print(board['mid-L']+ '|' + board['mid-M'] + '|' + board['mid-R'])
 print('-+-+-')
 print(board['low-L']+ '|' + board['low-M'] + '|' + board['low-R'])

def compMove():
  move = random.choice(list(board))
  if move in board and board[move] == ' ':
    board[move] = 'O'
    printBoard()

printBoard()



while True:
 move = input("Enter the position you want to place your X \n(top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R) or type 'quit' to exit: \n")
 if move in board and board[move] == ' ':
   board[move] = 'X'
   printBoard()
   compMove()
 if ['X', 'X', 'X'] in win:
    print("Congratulations! You win!")
    sys.exit()
 
 if move == 'quit':
    print("Thanks for playing!")
    sys.exit()
 elif move not in board:
    print("Must enter a vaild position\n")
    printBoard()
 
  
