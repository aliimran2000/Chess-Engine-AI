from Piece.piece import piece
import numpy as np
from copy import copy

# The Bishop can move any number of squares diagonally
# if its path is not blocked. Note that this Bishop starts on
# a light square and can reach only other light squares. At
# the beginning of the game, you have one ”dark-square”
# Bishop and one ”light-square” Bishop. The Bishop’s moves
# are shown by the highlighted squares in the following chess-
# board. This black Bishop can capture the white pawn but its path
# is blocked by the black Knight if it wants to move to the lower right.


class Bishop(piece):

    def __init__(self, color, pos):
        self.color = color
        self.position = pos
        self.name = "B"
        self.points = 3
        self.__moves = None

    def Move_To(self, pos):
        self.position = pos
        self.__moves = None

    def moves(self, piecesList):

        moves = []
        movesWithHits = []

        currentPosition = copy(self.position)

        # Forward position exists
        tempForwardPosition = self.moveforward(currentPosition)

        # For forward left
        while(self.isInBoard(tempForwardPosition)):

            tempForwardLeftPosition = self.moveleft(tempForwardPosition)

            # Left position exists
            if (self.isInBoard(tempForwardLeftPosition)):
                piece = self.Piece_Info(tempForwardLeftPosition, piecesList)

                # No piece already present, add to move list and continue
                if piece == None:
                    moves.append(tempForwardLeftPosition)
                # Enemy present, add to hit list and break
                else:
                    if piece.color != self.color:
                        movesWithHits.append(tempForwardLeftPosition)
                    break

            tempForwardPosition = tempForwardLeftPosition
            tempForwardPosition = self.moveforward(tempForwardPosition)

        # Forward position exists
        tempForwardPosition = self.moveforward(currentPosition)

        # For Forward right
        while(self.isInBoard(tempForwardPosition)):

            tempForwardRightPosition = self.moveright(tempForwardPosition)

            # Right position exists
            if (self.isInBoard(tempForwardRightPosition)):
                piece = self.Piece_Info(tempForwardRightPosition, piecesList)

                # No piece already present, add to move list and continue
                if piece == None:
                    moves.append(tempForwardRightPosition)
                # Enemy present, add to hit list and break
                else:
                    if piece.color != self.color:
                        movesWithHits.append(tempForwardRightPosition)
                    break

            tempForwardPosition = tempForwardRightPosition
            tempForwardPosition = self.moveforward(tempForwardPosition)

        # Backward position exists
        tempBackwardPosition = self.movebackward(currentPosition)

        # For backward left
        while(self.isInBoard(tempBackwardPosition)):

            tempBackwardLeftPosition = self.moveleft(tempBackwardPosition)

            # Left position exists
            if (self.isInBoard(tempBackwardLeftPosition)):
                piece = self.Piece_Info(tempBackwardLeftPosition, piecesList)

                # No piece already present, add to move list and continue
                if piece == None:
                    moves.append(tempBackwardLeftPosition)
                # Enemy present, add to hit list and break
                else:
                    if piece.color != self.color:
                        movesWithHits.append(tempBackwardLeftPosition)
                    break

            tempBackwardPosition = tempBackwardLeftPosition
            tempBackwardPosition = self.movebackward(tempBackwardPosition)

        # Backward position exists
        tempBackwardPosition = self.movebackward(currentPosition)

        # For Backward right
        while(self.isInBoard(tempBackwardPosition)):

            tempBackwardRightPosition = self.moveright(tempBackwardPosition)

            # Right position exists
            if (self.isInBoard(tempBackwardRightPosition)):
                piece = self.Piece_Info(tempBackwardRightPosition, piecesList)

                # No piece already present, add to move list and continue
                if piece == None:
                    moves.append(tempBackwardRightPosition)
                # Enemy present, add to hit list and break
                else:
                    if piece.color != self.color:
                        movesWithHits.append(tempBackwardRightPosition)
                    break

            tempBackwardPosition = tempBackwardRightPosition
            tempBackwardPosition = self.movebackward(tempBackwardPosition)

        if moves == [] and movesWithHits == []:
            self.__moves = None
        else:
            self.__moves = [moves, movesWithHits]
    
        return moves, movesWithHits
