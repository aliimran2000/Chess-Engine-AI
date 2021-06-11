from Piece.piece import piece
import numpy as np
from copy import copy

# The Rook is the next most powerful piece. The Rook can
# move any number of squares in one direction – vertically
# or horizontally– if its path is not blocked. For example, the
# squares this black Rook can move to are highlighted in the
# chessboard below. It can capture the white Pawn to its left
# but its path is blocked if it wants to move downward–by its
# black King.


class Rook(piece):

    def __init__(self, color, pos):
        self.color = color
        self.position = pos
        self.name = "R"
        self.points = 5
        self.__moves = None
        self.hasMoved = False

    def Move_To(self, pos):
        self.position = pos
        self.__moves = None
        self.hasMoved = True

    def moves(self, piecesList):

        moves = []
        movesWithHits = []

        currentPosition = copy(self.position)

        tempForwardPosition = self.moveforward(currentPosition)
        tempBackwardPosition = self.movebackward(currentPosition)
        tempLeftPosition = self.moveleft(currentPosition)
        tempRightPosition = self.moveright(currentPosition)

        # Till our rook can move upward
        # print(self.isInBoard(tempForwardPosition), tempForwardPosition)
        while(self.isInBoard(tempForwardPosition)):

            # Checking whether a piece is present on forward position
            piecePresent = self.Piece_Info(tempForwardPosition, piecesList)

            if piecePresent == None:
                moves.append(tempForwardPosition)
                tempForwardPosition = self.moveforward(tempForwardPosition)
                continue

            # If an enemy is present, add into hit moves list and break loop
            else:
                if piecePresent.color != self.color:
                    movesWithHits.append(tempForwardPosition)
                break

        # Till our rook can move back
        while(self.isInBoard(tempBackwardPosition)):

            # Checking whether a piece is present on Backward position
            piecePresent = self.Piece_Info(tempBackwardPosition, piecesList)

            if piecePresent == None:
                moves.append(tempBackwardPosition)
                tempBackwardPosition = self.movebackward(tempBackwardPosition)
                continue

            # If an enemy is present, add into hit moves list and break loop
            else:
                if piecePresent.color != self.color:
                    movesWithHits.append(tempBackwardPosition)
                break

        # Till our rook can move left
        while(self.isInBoard(tempLeftPosition)):

            # Checking whether a piece is present on left position
            piecePresent = self.Piece_Info(tempLeftPosition, piecesList)

            if piecePresent == None:
                moves.append(tempLeftPosition)
                tempLeftPosition = self.moveleft(tempLeftPosition)
                continue

            # If an enemy is present, add into hit moves list and break loop
            else:
                if piecePresent.color != self.color:
                    movesWithHits.append(tempLeftPosition)
                break

        # Till our rook can move right
        while(self.isInBoard(tempRightPosition)):

            # Checking whether a piece is present on right position
            piecePresent = self.Piece_Info(tempRightPosition, piecesList)

            if piecePresent == None:
                moves.append(tempRightPosition)
                tempRightPosition = self.moveright(tempRightPosition)
                continue

            # If an enemy is present, add into hit moves list and break loop
            else:
                if piecePresent.color != self.color:
                    movesWithHits.append(tempRightPosition)
                break

        if moves == [] and movesWithHits == []:
            self.__moves = None
        else:
            self.__moves = [moves, movesWithHits]

        return moves, movesWithHits
