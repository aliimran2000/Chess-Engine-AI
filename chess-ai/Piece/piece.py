from abc import ABC, abstractmethod
from copy import copy
# black pieces on top


class piece(ABC):

    def __init__(self, color):
        self.color = color
        self.points = -1
        self.position = [0, 0]
        self.__moves = None

    def __repr__(self):
        return self.color+self.name

    def isInBoard(self, move):
        
        if move[0] >= 0 and move[0] < 8:
            if move[1] >= 0 and move[1] < 8:
                return True

        return False

    def Piece_Info(self,pos,listofpieces):
        pass
        for piece in listofpieces:
            if piece.position == pos:
                return piece
        
        return None

    def Move_To(self,pos):
        
        self.__moves = None
        self.position = pos
        

    def moveforward(self, position):
        pos = copy(position)
        if self.color == 'b':
            pos[0] += 1

        if self.color == 'w':
            pos[0] -= 1

        return pos

    def movebackward(self, position):
        pos = copy(position)
        if self.color == 'b':
            pos[0] -= 1

        if self.color == 'w':
            pos[0] += 1

        return pos
    
    def moveright(self, position):
        pos = copy(position)
        if self.color == 'b':
            pos[1] -= 1

        if self.color == 'w':
            pos[1] += 1

        return pos

    def moveleft(self, position):
        pos = copy(position)
        if self.color == 'b':
            pos[1] += 1

        if self.color == 'w':
            pos[1] -= 1

        return pos

    def cleanMoves(self, piecesList):
        pass

    def moves(self, piecesList):
        #returns two arrays of moves and hits
        pass

   