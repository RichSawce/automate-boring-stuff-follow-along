#Tic Tac Toe Game

moveList = {"TL": [], "TM": [], "TR": [],
            "ML": [], "MM": [], "MR": [],
            "BL": [], "BM": [], "BR": []}

grid = moveList(['', '', ''],
                ['', '', ''],
                ['', '', ''])

user_input = moveList.values()




while True: 
 move = input("Enter your move: (TL, TM, TR, ML, MM, MR, BL, BM, BR) \n")
 if move in moveList:
    moveList[move].append("X")
    print(*grid)
 else:    print("Invalid move. Please try again.")
 
