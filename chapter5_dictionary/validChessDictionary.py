board = {'a1': 'wR', 'b1': 'wK', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wKing', 'f1': 'wB', 'g1': 'wK', 'h1': 'wR',
         'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP', 'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP',
         'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',
         'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',
         'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
         'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
         'a7': 'bP', 'b7': 'bP', 'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
         'a8': 'bR', 'b8': 'bK', 'c8': 'bB', 'd8': 'bQ', 'e8': 'bKing', 'f8': 'bB', 'g8': 'bK', 'h8': 'bR'}
def valid_pieces():
 pieces = ['wR', 'wK', 'wB', 'wQ', 'wKing', 'wP', ' ', 'bR', 'bK', 'bB', 'bQ', 'bKing', 'bP']
 for piece in board.values():
        if piece not in pieces:
            return False
 return True



condition1 = 'wKing' in board.values() and 'bKing' in board.values()
condition2 = all(key in board for key in ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']) and all(key in board for key in ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']) and all(key in board for key in ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3']) and all(key in board for key in ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4']) and all(key in board for key in ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5']) and all(key in board for key in ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6']) and all(key in board for key in ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']) and all(key in board for key in ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'])



print(valid_pieces())
