from Piece.piece import piece
import numpy as np
from copy import copy

# The Knight’s move is special. It hops directly from its old
# square to its new square. The Knight can jump over other
# pieces between its old and new squares. Think of the
# Knight’s move as an ”L.” It moves two squares horizontally
# or vertically and then makes a right-angle turn for one more
# square (“2 then 1”). The Knight always lands on a square
# opposite in color from its old square.


class Knight(piece):

    def __init__(self, color, pos):
        self.color = color
        self.position = pos
        self.name = "k"
        self.points = 3
        self.__moves = None


    def Move_To(self, pos):
        self.position = pos
        self.__moves = None


    def moves(self, piecesList):

        moves = []
        movesWithHits = []

        currentPosition = copy(self.position)

        forwardPosition = self.moveforward(currentPosition)
        backwardPosition = self.movebackward(currentPosition)
        leftPosition = self.moveleft(currentPosition)
        rightPosition = self.moveright(currentPosition)

        # POSSIBILITY 1 (UP UP LEFT/RIGHT)
        if(self.isInBoard(forwardPosition)):
            # 2 STEP UP
            forwardPosition = self.moveforward(forwardPosition)
            if(self.isInBoard(forwardPosition)):
                # LEFT POS
                newLeft = self.moveleft(forwardPosition)
                # RIGHT POS
                newRight = self.moveright(forwardPosition)

                if(self.isInBoard(newLeft)):
                    # EMPTY POS
                    piece = self.Piece_Info(newLeft, piecesList)

                    if piece == None:
                        moves.append(newLeft)
                    else:
                        # ENEMY
                        if piece.color != self.color:
                            movesWithHits.append(newLeft)

                if(self.isInBoard(newRight)):
                    # EMPTY POS
                    piece = self.Piece_Info(newRight, piecesList)

                    if piece == None:
                        moves.append(newRight)
                    else:
                        # ENEMY
                        if piece.color != self.color:
                            movesWithHits.append(newRight)

        # POSSIBILITY 2 (DOWN DOWN LEFT/RIGHT)
        if(self.isInBoard(backwardPosition)):
            # 2 STEP DOWN
            backwardPosition = self.movebackward(backwardPosition)
            if(self.isInBoard(backwardPosition)):
                # LEFT POS
                newLeft = self.moveleft(backwardPosition)
                # RIGHT POS
                newRight = self.moveright(backwardPosition)

                if(self.isInBoard(newLeft)):
                    # EMPTY POS
                    piece = self.Piece_Info(newLeft, piecesList)

                    if piece == None:
                        moves.append(newLeft)
                    else:
                        # ENEMY
                        if piece.color != self.color:
                            movesWithHits.append(newLeft)

                if(self.isInBoard(newRight)):
                    # EMPTY POS
                    piece = self.Piece_Info(newRight, piecesList)

                    if piece == None:
                        moves.append(newRight)
                    else:
                        # ENEMY
                        if piece.color != self.color:
                            movesWithHits.append(newRight)

        # POSSIBILITY 3 (LEFT LEFT UP/DOWN)
        if(self.isInBoard(leftPosition)):
            # 2 STEP LEFT
            leftPosition = self.moveleft(leftPosition)
            if(self.isInBoard(leftPosition)):
                # UP POS
                newUp = self.moveforward(leftPosition)
                # DOWN POS
                newDown = self.movebackward(leftPosition)

                if(self.isInBoard(newUp)):
                    # EMPTY POS
                    piece = self.Piece_Info(newUp, piecesList)

                    if piece == None:
                        moves.append(newUp)
                    else:
                        # ENEMY
                        if piece.color != self.color:
                            movesWithHits.append(newUp)

                if(self.isInBoard(newDown)):
                    # EMPTY POS
                    piece = self.Piece_Info(newDown, piecesList)

                    if piece == None:
                        moves.append(newDown)
                    else:
                        # ENEMY
                        if piece.color != self.color:
                            movesWithHits.append(newDown)

        # POSSIBILITY 4 (RIGHT RIGHT UP/DOWN)
        if(self.isInBoard(rightPosition)):
            # 2 STEP right
            rightPosition = self.moveright(rightPosition)
            if(self.isInBoard(rightPosition)):
                # UP POS
                newUp = self.moveforward(rightPosition)
                # DOWN POS
                newDown = self.movebackward(rightPosition)

                if(self.isInBoard(newUp)):
                    # EMPTY POS
                    piece = self.Piece_Info(newUp, piecesList)

                    if piece == None:
                        moves.append(newUp)
                    else:
                        # ENEMY
                        if piece.color != self.color:
                            movesWithHits.append(newUp)

                if(self.isInBoard(newDown)):
                    # EMPTY POS
                    piece = self.Piece_Info(newDown, piecesList)

                    if piece == None:
                        moves.append(newDown)
                    else:
                        # ENEMY
                        if piece.color != self.color:
                            movesWithHits.append(newDown)

        if moves == [] and movesWithHits == []:
            self.__moves = None
        else:
            self.__moves = [moves, movesWithHits]

        return moves, movesWithHits