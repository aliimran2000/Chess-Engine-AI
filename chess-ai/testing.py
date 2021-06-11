from board import Board
from utils.empty_boards import Init_Default_Board

ListPieces = Init_Default_Board()
b = Board(ListPieces)


print(b.get_board())

currentpos = [0,0]
for i in ListPieces:
    if i.position == currentpos :
        moves = (i.moves(ListPieces))
        print(moves)
        b.mark_moves(moves[0])
        #i.Move_To(moves[0][18])        


#b = Board(ListPieces)
print(b.get_board())


