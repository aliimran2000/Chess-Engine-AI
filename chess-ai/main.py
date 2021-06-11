from utils.Scripts import Pawn_to_Kukkar
import pygame as p
import sys

from board import Board
from utils.empty_boards import Init_Default_Board, Test_Queen, Test_Knight, Test_Rook, Test_Castling, Test_En_Passant, Test_Check, Init_Default_Board_1
from settings import _BOARDS_COLORS, _MY_COLOR, _O_COLOR
from Piece.Queen import Queen
from Piece.Knight import Knight
from Piece.Bishop import Bishop
from Piece.Rook import Rook

import logging

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='chess.log',
                    filemode='w',
                    level=logging.DEBUG)

logging.info("Starting LOG")


MAX_FPS = 15
_WINDOW_DIM = 512
_PIECE_SIZE = int(_WINDOW_DIM / 8)
_LIST_OF_PIECES = Init_Default_Board()
_BOARD_ = Board(_LIST_OF_PIECES)
_PIECE_NAMES = ['bR', 'bk', 'bB', 'bQ', 'bK',
                'bP', 'wP', 'wR', 'wk', 'wB', 'wQ', 'wK']
_IMAGES_ = dict()


def load_piece_images():
    global _IMAGES_
    global _PIECE_NAMES

    for image_name in _PIECE_NAMES:
        _IMAGES_[image_name] = p.transform.scale(p.image.load(
            "images/" + image_name + ".png"), (_PIECE_SIZE, _PIECE_SIZE))

    logging.info("images loaded")


def main():

    sys.setrecursionlimit(10000)
    p.init()
    p.display.set_caption("Smart-Chess")
    screen = p.display.set_mode((512, 512))
    screen.fill(p.Color("white"))
    clock = p.time.Clock()
    load_piece_images()

    # initializing board
    ListPieces = Init_Default_Board()
    #ListPieces = Test_En_Passant()
    board = Board(ListPieces)

    # initialzing game variables
    start = True
    moves, hitmoves, advanced_moves, en_passant = [], [], [None, None], []

    checkedboxes = []
    selected_piece = None
    selected = False
    Turn = 0

    while(start):

        if Turn == 1:
            for event in p.event.get():
                if event.type == p.QUIT:
                    start = False

                if event.type == p.MOUSEBUTTONDOWN:

                    y, x = event.pos

                    x = int(x/_PIECE_SIZE)
                    y = int(y/_PIECE_SIZE)

                    # clicked on the piece
                    if not selected:
                        moves, hitmoves, advanced_moves, en_passant = [], [], [None, None], []
                        # checkedboxes

                        selected_piece = None

                        for i in ListPieces:

                            if i.position == [x, y] and i.color == _MY_COLOR:
                                selected_piece = i

                                if selected_piece.name == "K":

                                    moves, hitmoves, advanced_moves = i.moves(
                                        ListPieces)

                                    moves, hitmoves, checkedboxes = board.Board_isCheck(
                                        selected_piece, moves, hitmoves, ListPieces)

                                    
                                    if moves == [] and hitmoves == [] and selected_piece.hasMoved() :
                                        p.quit()
                                        start = False
                                        print("CHECK MATE YOU LOST NOOB")
                                        logging.info("YOU LOST BY CHECKMATE")
                                        break

                                elif selected_piece.name == "P":
                                    try:
                                        moves, hitmoves, en_passant = i.moves(
                                            ListPieces, lastMoveRegisteredFrom, lastMoveBy)
                                    except:
                                        moves, hitmoves, en_passant = i.moves(
                                            ListPieces, None, None)

                                    tempList = []
                                    for m in moves:
                                        if not board.Board_isCheck_Non_King_Move(selected_piece, m, selected_piece.position):
                                            checkedboxes.append(m)
                                        else:
                                            tempList.append(m)
                                    moves = tempList

                                    tempList = []
                                    for m in hitmoves:
                                        if not board.Board_isCheck_Non_King_Move(selected_piece, m, selected_piece.position, True):
                                            checkedboxes.append(m)
                                        else:
                                            tempList.append(m)
                                    hitmoves = tempList

                                else:

                                    moves, hitmoves = i.moves(ListPieces)

                                    tempList = []
                                    for m in moves:
                                        if not board.Board_isCheck_Non_King_Move(selected_piece, m, selected_piece.position):
                                            checkedboxes.append(m)
                                        else:
                                            tempList.append(m)
                                    moves = tempList

                                    tempList = []
                                    for m in hitmoves:
                                        if not board.Board_isCheck_Non_King_Move(selected_piece, m, selected_piece.position, True):
                                            checkedboxes.append(m)
                                        else:
                                            tempList.append(m)
                                    hitmoves = tempList

                                selected = True
                                break

                    elif selected:
                        #print(moves, hitmoves)
                        if [x, y] in moves:
                            lastMoveRegisteredFrom = selected_piece.position
                            selected_piece.Move_To([x, y])
                            Turn = 0
                            lastMoveBy = selected_piece

                            logging.info(
                                f"Moved Piece {selected_piece} to [{x},{y}]")

                            if (selected_piece.name == "P") and (x == 7 or x == 0):

                                board.KickfromList_Position([x, y])
                                inp = input(
                                    "Enter q : Queen , k : Knight , b : Bishop , r : Rook")

                                if inp == 'k':

                                    board.Add_to_List(
                                        Knight(selected_piece.color, [x, y]))

                                elif inp == 'b':
                                    board.Add_to_List(
                                        Bishop(selected_piece.color, [x, y]))

                                elif inp == 'r':
                                    board.Add_to_List(
                                        Rook(selected_piece.color, [x, y]))
                                else:
                                    board.Add_to_List(
                                        Queen(selected_piece.color, [x, y]))

                                selected_piece = None

                        if [x, y] in hitmoves:
                            pees = board.KickfromList_Position([x, y])

                            if (selected_piece.name == "P") and (x == 7 or x == 0):

                                board.KickfromList(selected_piece)

                                inp = input(
                                    "Enter q : Queen , k : Knight , b : Bishop , r : Rook")

                                if inp == 'k':
                                    board.Add_to_List(
                                        Knight(selected_piece.color, [x, y]))

                                elif inp == 'b':
                                    board.Add_to_List(
                                        Bishop(selected_piece.color, [x, y]))

                                elif inp == 'r':
                                    board.Add_to_List(
                                        Rook(selected_piece.color, [x, y]))
                                else:
                                    board.Add_to_List(
                                        Queen(selected_piece.color, [x, y]))

                                selected_piece = None

                            else:
                                lastMoveRegisteredFrom = selected_piece.position
                                selected_piece.Move_To([x, y])
                                Turn = 0
                                lastMoveBy = selected_piece

                            logging.info(
                                f"{selected_piece} attacked {pees} @[{x},{y}]")

                        if [x, y] in en_passant:
                            board.KickfromList_Position(lastMoveBy.position)
                            selected_piece.Move_To([x, y])
                            Turn = 0
                            selected_piece = None

                        # LEFT SWAP
                        if advanced_moves[0] and [x, y] == advanced_moves[0][0]:
                            for piece in ListPieces:
                                if piece.name == "R" and piece.color == selected_piece.color:
                                    if piece.position == [selected_piece.position[0], 0]:
                                        piece.Move_To(advanced_moves[0][1])
                                        Turn = 0
                                        break
                            selected_piece.Move_To([x, y])
                            Turn = 0
                            selected_piece = None

                        # RIGHT SWAP
                        if advanced_moves[1] and [x, y] == advanced_moves[1][0]:
                            for piece in ListPieces:
                                if piece.name == "R" and piece.color == selected_piece.color:
                                    if piece.position == [selected_piece.position[0], 7]:
                                        piece.Move_To(advanced_moves[1][1])
                                        Turn = 0
                                        break
                            selected_piece.Move_To([x, y])
                            Turn = 0
                            selected_piece = None

                        selected = False
                        moves, hitmoves, advanced_moves, en_passant = [], [], [None, None], []
                        checkedboxes = []

                        # input()
                        selected_piece = None

                    board.update_board()
                

        elif Turn == 0:
            #board.isAIKingDying(board)
            print("AI Doing Turn")
            Turn = 1

            #mvs = board.generate_all_possible_moves('b', board)
            # logging.info(len(mvs))
            # for ms in mvs :
            #    logging.info(ms)

            #board = board.Random_AI_Move(_O_COLOR,board)
            #board = board.Intelligent_AI_Move(board)[0]
            vals = board.Intelligent_AI_Move()
            board = vals[0]

            # WE HAVE WON
            if board == None:
                p.quit()
                start = False
                print("CHECK MATE I HAVE WON")
                logging.info("YOU WON BY CHECKMATE")
                break

            hueristic = vals[1]
            print(hueristic)
            ListPieces = board.pieceslist
            board.pieceslist = Pawn_to_Kukkar(board.pieceslist)
            board.update_board()

        if board.Game_End():
            board.Winner()
            p.quit()

        Display_GAME(screen, board, moves, hitmoves,
                     advanced_moves, en_passant, checkedboxes)

        clock.tick(MAX_FPS)
        p.display.flip()


def Display_GAME(screen, board, moves, hitmoves, advanced_moves, en_passant, checkedboxes):
    pass
    Display_Board(screen, moves, hitmoves, advanced_moves,
                  en_passant, checkedboxes)
    Display_Pieces_on_Board(screen, board)


def Display_Board(screen, moves, hit, advanced_moves, en_passant, checkedboxes):

    b = True

    for i in range(8):

        for j in range(8):
            if b:
                p.draw.rect(screen, p.Color(_BOARDS_COLORS['board'][0]), p.Rect(
                    j*_PIECE_SIZE, i*_PIECE_SIZE, _PIECE_SIZE, _PIECE_SIZE))
                b = False

            else:
                p.draw.rect(screen, p.Color(_BOARDS_COLORS['board'][1]), p.Rect(
                    j*_PIECE_SIZE, i*_PIECE_SIZE, _PIECE_SIZE, _PIECE_SIZE))
                b = True

            if [i, j] in moves:
                p.draw.circle(screen, p.Color(_BOARDS_COLORS['moves']), (
                              j*_PIECE_SIZE+_PIECE_SIZE/2, i*_PIECE_SIZE+_PIECE_SIZE/2), _PIECE_SIZE-50)

            if [i, j] in hit:
                p.draw.rect(screen, p.Color(_BOARDS_COLORS['hit']), p.Rect(
                    j*_PIECE_SIZE, i*_PIECE_SIZE, _PIECE_SIZE, _PIECE_SIZE))

            if advanced_moves[0] != None:
                if [i, j] == advanced_moves[0][0]:
                    p.draw.circle(screen, p.Color(_BOARDS_COLORS['castling']), (
                        j*_PIECE_SIZE+_PIECE_SIZE/2, i*_PIECE_SIZE+_PIECE_SIZE/2), _PIECE_SIZE-50)

            if advanced_moves[1] != None:
                if [i, j] == advanced_moves[1][0]:
                    p.draw.circle(screen, p.Color(_BOARDS_COLORS['castling']), (
                        j*_PIECE_SIZE+_PIECE_SIZE/2, i*_PIECE_SIZE+_PIECE_SIZE/2), _PIECE_SIZE-50)

            if [i, j] in en_passant:
                p.draw.circle(screen, p.Color(_BOARDS_COLORS['en_passant']), (
                    j*_PIECE_SIZE+_PIECE_SIZE/2, i*_PIECE_SIZE+_PIECE_SIZE/2), _PIECE_SIZE-50)

            if [i, j] in checkedboxes:
                p.draw.circle(screen, p.Color(_BOARDS_COLORS['checkmate']), (
                    j*_PIECE_SIZE+_PIECE_SIZE/2, i*_PIECE_SIZE+_PIECE_SIZE/2), _PIECE_SIZE-50)

        if b:
            b = False
        else:
            b = True


def Display_Pieces_on_Board(screen, board):
    pass

    for i in range(8):
        for j in range(8):
            b = board.get_board()

            if b[i][j] != "**":
                screen.blit(_IMAGES_[b[i][j]], p.Rect(
                    j*_PIECE_SIZE, i*_PIECE_SIZE, _PIECE_SIZE, _PIECE_SIZE))


main()
