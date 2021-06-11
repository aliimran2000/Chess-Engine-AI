from Piece.piece import piece
import numpy as np
from copy import copy


# The Pawn moves straight ahead (never backward), but it
# captures diagonally. It moves one square at a time, but on
# its first move it has the option of moving forward one or two
# squares. In the diagram, the highlighted squares indicate
# possible destinations for the pawns. The White pawn is on
# its original square, so it may move ahead either one or two
# squares. The black Pawn has already moved, so it may move
# ahead only one square at a time or capture diagonally. The

# squares on which these black Pawn may capture are indi-
# cated by arrows. If a pawn advances all the way to the op-
# posite end of the board, it is immediately ”promoted” to an-
# other piece, usually a Queen. It may not remain a pawn or

# become a King. Therefore, it is possible for each player to

# have more than one Queen or more than two Rooks, Bish-
# ops, or Knights on the board at the same time.

class Pawn(piece):

    def __init__(self, color, pos):
        self.color = color
        self.position = pos
        self.name = "P"
        self.points = 1
        self.FirstTurn = True
        self.__moves = None

    def Move_To(self, pos):
        
        self.FirstTurn = False
        self.position = pos
        self.__moves = None

    def moves(self, listOfPieces, lastMoveFrom = None, lastMoveBy = None):
        
        # list of moves possible
        moves = []
        movesWithHits = []
        en_passant = []

        currentPosition = copy(self.position)

        # Possible moves of First Turn
        newPosition = self.moveforward(currentPosition)
        if self.FirstTurn:

            if self.Piece_Info(newPosition, listOfPieces) == None:
                # moves.append(newPosition)

                nfrwrdpos = self.moveforward(newPosition)

                if self.Piece_Info(nfrwrdpos, listOfPieces) == None:
                    moves.append(nfrwrdpos)

        P = self.Piece_Info(newPosition, listOfPieces)

        # If no piece in is in front of current piece, then move forward
        if P == None:
            moves.append(newPosition)

        # Checking if we can hit an opponent piece
        diagonalMoves = []

        tempForwardPosition = self.moveforward(currentPosition)
        diagonalMoves.append(self.moveright(tempForwardPosition))
        diagonalMoves.append(self.moveleft(tempForwardPosition))

        rightDiagonal = self.Piece_Info(diagonalMoves[0], listOfPieces)
        if rightDiagonal is not None:
            if rightDiagonal.color != self.color:
                movesWithHits.append(diagonalMoves[0])

        leftDiagonal = self.Piece_Info(diagonalMoves[1], listOfPieces)
        if leftDiagonal is not None:
            if leftDiagonal.color != self.color:
                movesWithHits.append(diagonalMoves[1])

        moves = [i for i in moves if self.isInBoard(i)]

        #CALCULATING EN_PASSANT MOVE
        tempForward = self.moveforward(currentPosition)
        if lastMoveBy != None and not self.FirstTurn:
            newHitPos1 = self.moveright(moves[0])
            newHitPos2 = self.moveleft(moves[0])

            skippedPos = self.movebackward(lastMoveFrom)

            if self.isInBoard(skippedPos):
                if self.isInBoard(newHitPos1):
                    if skippedPos == newHitPos1 and lastMoveBy.name == "P" and lastMoveBy.color != self.color:
                        if newHitPos1 not in movesWithHits:
                            en_passant.append(newHitPos1)

                if self.isInBoard(newHitPos2):
                    if skippedPos == newHitPos2 and lastMoveBy.name == "P" and lastMoveBy.color != self.color:
                        if newHitPos2 not in movesWithHits:
                            en_passant.append(newHitPos2)

        if moves == [] and movesWithHits == [] and en_passant == []:
            self.__moves = None
        else:
            self.__moves = [moves, movesWithHits, en_passant]


        return moves, movesWithHits, en_passant
