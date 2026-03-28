#Tic Tac Toe Game


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

printBoard()


while True:
 move = input("Enter the position you want to place your X \n(top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R) or type 'quit' to exit: \n")
 if move in board:
   board[move] = 'X'
   printBoard() 
 if board[move] == win:
    print("Congratulations! You win!")
 if move not in board and move != 'quit':
    print("Must enter a vaild position\n")
 if move == 'quit':
   break
