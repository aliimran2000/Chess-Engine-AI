from Piece.piece import piece
import numpy as np
from copy import copy

# The King is the most important piece. When it is trapped,
# the whole team loses. The King can move one square in any
# direction - for example, to any of the highlighted squares in
# this diagram. (An exception is castling, which is explained
# later.) The King may never move into check - that is, onto a
# square attacked by an opponent’s piece.


class King(piece):

    def __init__(self, color, pos):
        self.color = color
        self.position = pos
        self.name = "K"
        self.points = 1000
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

        forwardPosition = self.moveforward(currentPosition)
        backwardPosition = self.movebackward(currentPosition)
        leftPosition = self.moveleft(currentPosition)
        rightPosition = self.moveright(currentPosition)

        forwardLeftPosition = None
        forwardRightPosition = None

        backwardLeftPosition = None
        backwardRightPosition = None

        # LEFT
        if(self.isInBoard(leftPosition)):
            piecePresent = self.Piece_Info(leftPosition, piecesList)

            if piecePresent == None:
                moves.append(leftPosition)

            # If an enemy is present, add into hit moves list and break loop
            else:
                if piecePresent.color != self.color:
                    movesWithHits.append(leftPosition)

        # RIGHT
        if(self.isInBoard(rightPosition)):
            piecePresent = self.Piece_Info(rightPosition, piecesList)

            if piecePresent == None:
                moves.append(rightPosition)

            # If an enemy is present, add into hit moves list and break loop
            else:
                if piecePresent.color != self.color:
                    movesWithHits.append(rightPosition)

        # UP
        if(self.isInBoard(forwardPosition)):

            forwardLeftPosition = self.moveleft(forwardPosition)
            forwardRightPosition = self.moveright(forwardPosition)

            if not self.isInBoard(forwardLeftPosition):
                forwardLeftPosition = None
            if not self.isInBoard(forwardRightPosition):
                forwardRightPosition = None

            piecePresent = self.Piece_Info(forwardPosition, piecesList)
            leftPiecePresent = self.Piece_Info(forwardLeftPosition, piecesList)
            rightPiecePresent = self.Piece_Info(
                forwardRightPosition, piecesList)

            if piecePresent == None:
                moves.append(forwardPosition)

            # If an enemy is present, add into hit moves list and break loop
            else:
                if piecePresent.color != self.color:
                    movesWithHits.append(forwardPosition)

            if leftPiecePresent == None:
                moves.append(forwardLeftPosition)

            # If an enemy is present, add into hit moves list and break loop
            else:
                if leftPiecePresent.color != self.color:
                    movesWithHits.append(forwardLeftPosition)

            if rightPiecePresent == None:
                moves.append(forwardRightPosition)

            # If an enemy is present, add into hit moves list and break loop
            else:
                if rightPiecePresent.color != self.color:
                    movesWithHits.append(forwardRightPosition)

        # DOWN
        if(self.isInBoard(backwardPosition)):

            backwardLeftPosition = self.moveleft(backwardPosition)
            backwardRightPosition = self.moveright(backwardPosition)

            if not self.isInBoard(backwardLeftPosition):
                backwardLeftPosition = None
            if not self.isInBoard(backwardRightPosition):
                backwardRightPosition = None

            piecePresent = self.Piece_Info(backwardPosition, piecesList)
            leftPiecePresent = self.Piece_Info(
                backwardLeftPosition, piecesList)
            rightPiecePresent = self.Piece_Info(
                backwardRightPosition, piecesList)

            if piecePresent == None:
                moves.append(backwardPosition)

            # If an enemy is present, add into hit moves list and break loop
            else:
                if piecePresent.color != self.color:
                    movesWithHits.append(backwardPosition)

            if leftPiecePresent == None:
                moves.append(backwardLeftPosition)

            # If an enemy is present, add into hit moves list and break loop
            else:
                if leftPiecePresent.color != self.color:
                    movesWithHits.append(backwardLeftPosition)

            if rightPiecePresent == None:
                moves.append(backwardRightPosition)

            # If an enemy is present, add into hit moves list and break loop
            else:
                if rightPiecePresent.color != self.color:
                    movesWithHits.append(backwardRightPosition)

        # Calculate castling moves if king has not moved
        # if self.hasMoved == True:
        #     castleMoves = [None, None]
        # else:
        #     castleMoves = self.castlingMoves(piecesList)
        #     #print("ese : " , castleMoves)
        castleMoves = [None, None]

        if moves == [] and movesWithHits == [] and castleMoves == [None, None]:
            self.__moves = None
        else:
            self.__moves = [moves, movesWithHits, castleMoves]

        return moves, movesWithHits, castleMoves

    def checkCastleIntoCheck(self, newPos, piecesList, oldPos):

        for temp in piecesList:
            if temp.position == oldPos:
                thatPiece = temp
                temp.position = newPos
                break

        for piece in piecesList:
            # Selecting opponent pieces
            if piece.color != self.color:

                # CALCULATING THEIR MOVES
                if piece.name == "K":
                    moves, hitmoves, advancedmoves = piece.moves(piecesList)
                elif piece.name == "P":
                    moves, hitmoves, en_passant = piece.moves(
                        piecesList)
                else:
                    moves, hitmoves = piece.moves(piecesList)

                if newPos in hitmoves:
                    thatPiece.position = oldPos
                    return True

        thatPiece.position = oldPos
        return False

    def checkCastleThroughCheck(self, oldPos, newPos, piecesList):

        for piece in piecesList:
            # Selecting opponent pieces
            if piece.color != self.color:

                if newPos[1] > oldPos[1]:
                    for positionY in range(oldPos[1] + 1, newPos[1], 1):

                        for temp in piecesList:
                            if temp.position == oldPos:
                                thatPiece = temp
                                temp.position = [newPos[0], positionY]
                                break

                        # CALCULATING THEIR MOVES
                        if piece.name == "K":
                            moves, hitmoves, advancedmoves = piece.moves(
                                piecesList)
                        elif piece.name == "P":
                            moves, hitmoves, en_passant = piece.moves(
                                piecesList)
                        else:
                            moves, hitmoves = piece.moves(piecesList)

                        if [oldPos[0], positionY] in hitmoves:
                            thatPiece.position = oldPos
                            return True

                        thatPiece.position = oldPos

                if newPos[1] < oldPos[1]:
                    for positionY in range(newPos[1] + 1, oldPos[1], 1):
                        for temp in piecesList:
                            if temp.position == oldPos:
                                thatPiece = temp
                                temp.position = [newPos[0], positionY]
                                break

                        # CALCULATING THEIR MOVES
                        if piece.name == "K":
                            moves, hitmoves, advancedmoves = piece.moves(
                                piecesList)
                        elif piece.name == "P":
                            moves, hitmoves, en_passant = piece.moves(
                                piecesList)
                        else:
                            moves, hitmoves = piece.moves(piecesList)

                        if [oldPos[0], positionY] in hitmoves:
                            thatPiece.position = oldPos
                            return True

                        thatPiece.position = oldPos
        return False

    def checkCastleOutOfCheck(self, pos, piecesList):
        for piece in piecesList:
            # Selecting opponent pieces
            if piece.color != self.color:

                # CALCULATING THEIR MOVES
                if piece.name == "K":
                    moves, hitmoves, advancedmoves = piece.moves(piecesList)
                elif piece.name == "P":
                    moves, hitmoves, en_passant = piece.moves(
                        piecesList)
                else:
                    moves, hitmoves = piece.moves(piecesList)

                if pos in hitmoves:
                    return True

        return False

    def castlingMoves(self, piecesList):

        castleMoves = [None, None]

        # Check whether left and right rook has moved
        leftRookPos = [self.position[0], 0]
        rightRookPos = [self.position[0], 7]

        leftRook = self.Piece_Info(leftRookPos, piecesList)
        rightRook = self.Piece_Info(rightRookPos, piecesList)

        # Left Piece is present
        if leftRook != None:
            #it is rook
            if leftRook.name == "R":
                # it has not moved
                if leftRook.hasMoved == False:
                    # No piece is present between them
                    x = self.position[0]
                    piecePresent = False
                    for y in range(1, self.position[1]):
                        piece = self.Piece_Info([x, y], piecesList)
                        if piece is not None:
                            piecePresent = True
                            break
                    if piecePresent == False:
                        newCastleMove = []
                        newKingPos = [self.position[0], self.position[1] - 2]
                        newLRookPos = [self.position[0], newKingPos[1] + 1]
                        newCastleMove.append(newKingPos)
                        newCastleMove.append(newLRookPos)
                        castleMoves[0] = newCastleMove

                        # Filtering the move if castle out of check
                        if self.checkCastleIntoCheck(newKingPos, piecesList, self.position):
                            castleMoves[0] = None
                        elif self.checkCastleOutOfCheck(self.position, piecesList):
                            castleMoves[0] = None
                        elif self.checkCastleThroughCheck(self.position, newKingPos, piecesList):
                            castleMoves[0] = None

        # Right Piece is present
        if rightRook != None:
            #it is rook
            if rightRook.name == "R":

                # it has not moved
                if rightRook.hasMoved == False:
                    # No piece is present between them
                    x = self.position[0]
                    piecePresent = False
                    for y in range(6, self.position[1], -1):
                        piece = self.Piece_Info([x, y], piecesList)
                        if piece is not None:
                            piecePresent = True
                            break
                    if piecePresent == False:
                        newCastleMove = []
                        newKingPos = [self.position[0], self.position[1] + 2]
                        newRRookPos = [self.position[0], newKingPos[1] - 1]
                        newCastleMove.append(newKingPos)
                        newCastleMove.append(newRRookPos)
                        castleMoves[1] = newCastleMove

                        # Filtering the move if castle out of check
                        if self.checkCastleIntoCheck(newKingPos, piecesList, self.position):
                            castleMoves[1] = None
                        elif self.checkCastleOutOfCheck(self.position, piecesList):
                            castleMoves[1] = None
                        elif self.checkCastleThroughCheck(self.position, newKingPos, piecesList):
                            castleMoves[1] = None

        return castleMoves
