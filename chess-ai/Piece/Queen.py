from Piece.piece import piece
import numpy as np
from copy import copy

# The Queen can move in a straight line any number of
# squares in any one direction - horizontal, vertical, or diago-
# nal as long as its path is not blocked by its own pieces. It can
# capture a piece of the opposite color in its path. Below, the
# black Queen can reach any of the highlighed squares shown
# in this diagram. It can capture the white Rook but its path is
# blocked in some directions–below by the black King and to
# the lower right by the black Knight.


class Queen(piece):

    def __init__(self, color, pos):
        self.color = color
        self.position = pos
        self.name = "Q"
        self.points = 9
        self.__moves = None

    def Move_To(self, pos):
        self.position = pos
        self.__moves = None


    def moves(self, piecesList):

        moves = []
        movesWithHits = []

        currentPosition = copy(self.position)

        tempForwardPosition = self.moveforward(currentPosition)
        tempBackwardPosition = self.movebackward(currentPosition)
        tempLeftPosition = self.moveleft(currentPosition)
        tempRightPosition = self.moveright(currentPosition)

        # Till our rook can move upward
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
