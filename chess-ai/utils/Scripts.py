
from Piece.Queen import Queen


def KickfromList_Position(pos, list):
    for pees in list:
        if pees.position == pos:

            list.remove(pees)
            return str(pees)


def Pawn_to_Kukkar(lista):
    templista = []
    for p in lista:

        if (p.name == "P") and (p.position[0] == 7 or p.position == [0]):
            pass
            templista.append(Queen(p.color, p.position))
        else:
            templista.append(p)

    list = templista
    return templista


'''
if check or check mate
who's turn 
whos won

'''


def GameStatus(board, ListPieces):
    pass
