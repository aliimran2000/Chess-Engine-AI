from Piece.Bishop import Bishop
from Piece.King import King
from Piece.Queen import Queen
from Piece.Knight import Knight
from Piece.Rook import Rook
from Piece.Pawn import Pawn


def Init_Default_Board():
    ListPieces = [Rook('b', [0, 0]), Rook('b', [0, 7]), Knight('b', [0, 1]), Knight(
        'b', [0, 6]), Bishop('b', [0, 2]), Bishop('b', [0, 5]), Queen('b', [0, 3]), King('b', [0, 4])]
    ListPieces.extend([Pawn('b', [1, i]) for i in range(0, 8)])
    ListPiecesWhite = [Rook('w', [7, 0]), Rook('w', [7, 7]), Knight('w', [7, 1]), Knight(
        'w', [7, 6]), Bishop('w', [7, 2]), Bishop('w', [7, 5]), Queen('w', [7, 3]), King('w', [7, 4])]
    ListPiecesWhite.extend([Pawn('w', [6, i]) for i in range(0, 8)])
    ListPieces.extend(ListPiecesWhite)

    return ListPieces


def Init_Default_Board_1():
    ListPieces = [Rook('w', [7, 0]), Pawn('b', [6, 1]),
                  King('b', [4, 4]), King('w', [0, 0])]
    return ListPieces


def Test_Castling():
    ListPieces = [Rook('b', [0, 0]), Rook('b', [0, 7]), Queen('b', [0, 3]) , King('b', [0, 5])]
    ListPiecesWhite = [Rook('w', [7, 0]), Rook('w', [7, 7]), King('w', [7, 4])]
    ListPieces.extend(ListPiecesWhite)

    return ListPieces


def Test_Check():
    ListPieces = [Queen('b', [0, 0]), Queen('b', [0, 7])]
    ListPiecesWhite = [Rook('w', [7, 0]), Rook('w', [7, 7]), King('w', [7, 4])]
    ListPieces.extend(ListPiecesWhite)

    return ListPieces


def Test_En_Passant():
    ListPieces = [Pawn('b', [3, 2]), Rook('b', [0, 7])]
    ListPiecesWhite = [Pawn('w', [6, 3]),King('w',[7,7]),King('b',[0,0])]
    ListPieces.extend(ListPiecesWhite)

    return ListPieces


def Test_Rook():

    ListPieces = [Rook('b', [0, 0]), Rook('b', [0, 7]), Knight('b', [0, 1])]
    ListPieces.extend([Pawn('b', [1, i]) for i in range(0, 8)])
    ListPiecesWhite = [Bishop('w', [4, 5]), Rook('w', [7, 7]), Knight('w', [7, 1]), Knight(
        'w', [7, 6]), Bishop('w', [4, 0]), Bishop('w', [7, 5]), Queen('w', [7, 3]), King('w', [7, 4])]
    ListPiecesWhite.extend([Pawn('w', [2, i]) for i in range(1, 5)])
    ListPieces.extend(ListPiecesWhite)

    return ListPieces


def Test_Queen():
    pass
    ListP = [Queen("w", [3, 4]), Bishop("w", [6, 4]), Bishop("w", [1, 4]), Bishop(
        "w", [3, 6]), Bishop("w", [1, 3]), Bishop("b", [0, 1]), Rook("b", [7, 2]), Rook("w", [7, 1])]
    return ListP


def Test_Knight():
    pass
    ListP = [Knight("b", [3, 3]), Knight("w", [1, 4])]
    return ListP


def Test_King():
    pass
    ListP = [King("b", [0, 0]), Knight("w", [1, 1]), ]
    return ListP
