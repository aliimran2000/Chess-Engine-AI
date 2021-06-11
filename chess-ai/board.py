import numpy as np
import random
from copy import deepcopy
from settings import _AI_LEVEL, _O_COLOR
from Piece.Bishop import Bishop
from Piece.King import King
from Piece.Queen import Queen
from Piece.Knight import Knight
from Piece.Rook import Rook
from Piece.Pawn import Pawn

class Board:

    def __init__(self, pieceslist):
        self.checkState = False
        self.piecesOnBoard = pieceslist
        self.board = np.array(["**" for i in range(64)]).reshape((8, 8))
        self.pieceslist = pieceslist

        self.blackscore = 0
        self.whitescore = 0

        for all in self.pieceslist:
            self.board[all.position[0], all.position[1]] = all.__repr__()
            if all.color == 'w':
                self.whitescore += all.points

            elif all.color == 'b':
                self.blackscore += all.points

    def refresh_to(self, pieceslist):
        self.piecesOnBoard = pieceslist
        self.board = np.array(["**" for i in range(64)]).reshape((8, 8))
        self.pieceslist = pieceslist

        self.blackscore = 0
        self.whitescore = 0

        for all in self.pieceslist:
            self.board[all.position[0], all.position[1]] = all.__repr__()
            if all.color == 'w':
                self.whitescore += all.points

            elif all.color == 'b':
                self.blackscore += all.points

    def update_board(self):

        self.board = np.array(["**" for i in range(64)]).reshape((8, 8))

        for all in self.pieceslist:
            self.board[all.position[0], all.position[1]] = all.__repr__()

    def KickfromList_Position(self, pos):
        for pees in self.pieceslist:
            if pees.position == pos:

                if pees.color == 'w':
                    self.whitescore -= pees.points
                elif pees.color == 'b':
                    self.blackscore -= pees.points

                self.pieceslist.remove(pees)

                return str(pees)

    def KickfromList(self, pees):

        if pees.color == 'w':
            self.whitescore -= pees.points
        elif pees.color == 'b':
            self.blackscore -= pees.points

        self.pieceslist.remove(pees)

        return str(pees)

    def Add_to_List(self, Piece1):
        self.pieceslist.append(Piece1)
        if Piece1.color == 'w':
            self.whitescore += Piece1.points
        elif Piece1.color == 'b':
            self.blackscore += Piece1.points

    '''
    all moves are passed including hit and mmove arrays not advanced mvoes
    return array for both arrays in after check
    '''

    def Board_isCheck(self, King1, moveslist, hitslist, ListPieces):
        pass

        moves, hits = [], []
        nogo = []

        pieces = [
            pieces for pieces in self.pieceslist if pieces.color != King1.color]

        pm = []
        for p in pieces:
            parr = p.moves(ListPieces)
            pm.extend(parr[0])
            pm.extend(parr[1])

        for m in moveslist:
            if m not in pm:
                moves.append(m)
            else:
                nogo.append(m)

        for m in hitslist:
            if m not in pm:
                hits.append(m)
            else:
                nogo.append(m)

        return moves, hits, nogo

    def Board_isCheck_Non_King_Move(self, piece, newPos, oldPos, hitMove=False):

        myKing = None
        for aPiece in self.pieceslist:
            if aPiece.color == piece.color and aPiece.name == "K":
                myKing = aPiece
                break

        if (myKing == None):
            return True

        # # IF KING IS ALREADY BEING ATTACKED WITHOUT MOVING TO NEW POSITION
        enemyPieces = []
        for aPiece in self.pieceslist:
            if aPiece.color != piece.color:
                enemyPieces.append(aPiece)

        # for aPiece in enemyPieces:
        #     enemyHitMoves = aPiece.moves(self.pieceslist)[1]
        #     if myKing.position in enemyHitMoves:
        #         return True

        # NOW CHECK AFTER MOVING TO NEW POSITION
        piece.position = newPos

        canFilter = False
        numHits = 0

        for aPiece in enemyPieces:
            enemyHitMoves = aPiece.moves(self.pieceslist)[1]
            if myKing.position in enemyHitMoves:

                # CHECKING SCENARIO FOR HIT MOVE
                if hitMove == True:
                    canFilter = True
                    numHits += 1

                else:
                    piece.position = oldPos
                    return False

        piece.position = oldPos

        if canFilter == True and numHits == 1:
            return True
        elif canFilter == True and numHits > 1:
            return False
        elif canFilter == False:
            return True

    def get_board(self):
        return self.board

    def mark_moves(self, listmoves):
        for i in listmoves:
            if i != None:
                self.board[i[0], i[1]] = "$$"

    def get_moves(self, color):

        moves = []
        for pieces in self.piecesOnBoard:
            if pieces != None:
                if pieces.color == color:
                    moves.append(pieces.moves(self.piecesOnBoard))

        return moves

    def Get_Heuristic_difference(self, color):
        if color == 'w':
            return self.whitescore - self.blackscore

        if color == 'b':
            return self.blackscore - self.whitescore

    def createBoardCopy(self, listofpieces, MyBoard):

        newList = []
        for one in listofpieces:
            if one.name == "B":
                newList.append(Bishop(one.color, one.position))
            elif one.name == "K":
                PP = King(one.color, one.position)
                PP.hasMoved = one.hasMoved
                newList.append(PP)
            elif one.name == "k":
                newList.append(Knight(one.color, one.position))
            elif one.name == "P":
                PP = Pawn(one.color, one.position)
                PP.FirstTurn = one.FirstTurn
                newList.append(PP)
            elif one.name == "Q":
                newList.append(Queen(one.color, one.position))
            elif one.name == "R":
                PP = Rook(one.color, one.position)
                PP.hasMoved = one.hasMoved
                newList.append(PP)

        B = Board(newList)

        if B.board.dtype != None:
            B.board = np.array(["**" for i in range(64)]).reshape((8, 8))
            B.checkState = MyBoard.checkState

        return B

    # parrallelizeable
    def generate_all_move_pees(self, pees, board):
        c = pees.color

        listofpieces = [all for all in board.pieceslist]

        listofboards = []
        Nmoves = pees.moves(listofpieces)

        for m in Nmoves[0]:
            B = self.createBoardCopy(listofpieces, board)

            for n in B.pieceslist:

                if n.position == pees.position:
                    n.Move_To(m)
                    # B.update_board()
                    self.isAIKingDying(B)
                    if not B.checkState:
                        listofboards.append(B)
                        break

        for m in Nmoves[1]:

            B = self.createBoardCopy(listofpieces, board)

            for n in B.pieceslist:
                if n.position == pees.position:
                    B.KickfromList_Position(m)
                    n.Move_To(m)
                    # B.update_board()
                    self.isAIKingDying(B)
                    if not B.checkState:
                        listofboards.append(B)
                        break

        return listofboards

    def isAIKingDying(self, board):
        MYPieces = [all for all in board.pieceslist if all.color == 'b']
        
        for piece in board.pieceslist:
            if piece.color == 'w' and piece.name == 'K':
                enemyKing = piece
                break

        for piece in MYPieces:
            allMoves = piece.moves(board.pieceslist)

            if allMoves != None:
                if allMoves[1] != None and allMoves[1] != []:
                    for mov in allMoves[1]:
                        if mov == enemyKing.position:
                            board.checkState = True
                            return

        board.checkState = False

    def generate_all_possible_moves(self, color, board):

        listofboards = []
        colorpieces = [all for all in board.pieceslist if all.color == color]
        # print(colorpieces)

        for p in colorpieces:
            # print("yeet")
            listofboards.extend(board.generate_all_move_pees(p, board))

        return listofboards
        # return sorted(listofboards,key = lambda x : x.Get_Heuristic_difference(color))

    def Random_AI_Move(self, color, board):
        B = board.generate_all_possible_moves(color, board)
        b = random.choice(B)

        return b

    def Intelligent_AI_Move(self, color=_O_COLOR, depth=_AI_LEVEL['MOVES_DEPTH']):

        newBoard = self.createBoardCopy(self.pieceslist, self)
        return MIN_MAX(depth, self)

    def Game_End(self):
        if self.whitescore < 1000 or self.blackscore < 1000:
            return True
        return False

    def Winner(self):
        if (self.blackscore > self.whitescore) and _O_COLOR == 'b':
            print("YOU LOSE")

        if (self.blackscore < self.whitescore) and _O_COLOR == 'b':
            print("YOU WIN!!!!")

        if (self.blackscore < self.whitescore) and _O_COLOR == 'w':
            print("YOU LOSE")

        if (self.blackscore > self.whitescore) and _O_COLOR == 'w':
            print("YOU WIN!!!!")


def MIN_MAX(depth, board, MoveChoice=True, alpha=-np.inf, beta=np.inf):
    if depth == 0 or board.Game_End():
        return None, board.Get_Heuristic_difference(_O_COLOR)

    moves = board.generate_all_possible_moves(_O_COLOR, board)
    random.shuffle(moves)
    try:
        BestGeneratedMoves = random.choice(moves)
    except:
        print("YOU WON, AI LOST")
        exit(0)

    if MoveChoice:  # true for max
        val_max = -np.inf

        for move in moves:
            active_value = MIN_MAX(depth-1, move, False, alpha, beta)[1]

            if active_value > val_max:
                val_max = active_value
                BestGeneratedMoves = move
            alpha = max(alpha, active_value)
            if beta <= alpha:
                break
        return BestGeneratedMoves, val_max
    else:
        val_min = np.inf
        for move in moves:
            active_value = MIN_MAX(depth-1, move, True, alpha, beta)[1]

            if active_value < val_min:
                val_min = active_value
                BestGeneratedMoves = moves
            beta = min(beta, active_value)
            if beta <= alpha:
                break
        return BestGeneratedMoves, val_min
