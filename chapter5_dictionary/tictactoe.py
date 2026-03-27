#Tic Tac Toe Game

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard():
 print(board['top-L']+ '|' + board['top-M'] + '|' + board['top-R'])
 print('-+-+-')
 print(board['mid-L']+ '|' + board['mid-M'] + '|' + board['mid-R'])
 print('-+-+-')
 print(board['low-L']+ '|' + board['low-M'] + '|' + board['low-R'])

printBoard()


while True:
 move = input("Place your X \n")
 if move in board:
   board[move] = 'X'
   printBoard()
 elif move == '':
  print("Must enter X\n")
 elif move == 'quit':
  break
  
