# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# Hoppers game.py

from board import Board
from game_options import PLAYER_1_COLOR,PLAYER_2_COLOR
import copy
import pandas
import itertools

class Game:
    def __init__(self,display=None):
        self.board = Board(display)
        self.turn = PLAYER_1_COLOR
        self.selectedPiece = 0
        self.possibleMoves = []
        self.possibleDestinations = []


    def copy(self):
        return copy.deepcopy(self)

    def move(self,fromRow,fromCol,row,col,display=None):
        self.board.move(fromRow,fromCol,row,col,display)
        self.selectedPiece = 0
        self.changeTurn()
        return self.copy()

    #Move from action
    def moveAction(self,action,printPath=False,display=None):
        initSpace= action.checkRootSpace()
        endSpace = action
        self.board.move(initSpace.currentRow,initSpace.currentCol,endSpace.currentRow,endSpace.currentCol,display)
        self.selectedPiece = 0
        self.changeTurn()
        return self.copy()
    
    def moveActionCopy(self,action,printPath=False,display=None):
        gameCopy = self.copy()
        initSpace= action.checkRootSpace()
        endSpace = action
        gameCopy.move(initSpace.currentRow,initSpace.currentCol,endSpace.currentRow,endSpace.currentCol,display)
        gameCopy.selectedPiece = 0
        gameCopy.changeTurn()
        return gameCopy

    def checkPossibleMoves(self):
        if(self.turn==PLAYER_1_COLOR):
            return list(itertools.chain.from_iterable(map(self.checkPossibleMovesPiece,self.board.piecesPlayer1)))
        else:
            return list(itertools.chain.from_iterable(map(self.checkPossibleMovesPiece,self.board.piecesPlayer2)))


    def checkPossibleMovesPiece(self,piece):
        return piece.possibleMoves(self.board)


    def toMoveTurn(self):
        return self.turn



    def selectPiece(self,row,col,display=None):
        self.possibleDestinations=[]
        self.possibleMoves=[]
        self.selectedPiece = self.board.getPiece(row,col)
        self.board.drawBoard(display)
        if(self.selectedPiece!=0 and self.selectedPiece.color==self.turn):
            self.selectedPiece.drawSelected(display)
            self.possibleDestinations,self.possibleMoves=self.board.drawPossibleMoves(self.selectedPiece,display)
        else:
            self.selectedPiece =0

    def changeTurn(self):
        if self.turn==PLAYER_1_COLOR:
            self.turn=PLAYER_2_COLOR
        else:
            self.turn=PLAYER_1_COLOR

    def checkWin(self):
        player1PiecesInPlayer2House = 0
        player2PiecesInPlayer1House = 0
        player1PiecesInPlayer1House = 0
        player2PiecesInPlayer2House = 0
        for i in range(len(self.board.piecesPlayer1)):
            piecePlayer1 = self.board.piecesPlayer1[i]
            piecePlayer2 = self.board.piecesPlayer2[i]
            #Check pieces player 1 count
            if(piecePlayer1.row+piecePlayer1.col<=4):
                player1PiecesInPlayer1House = player1PiecesInPlayer1House+1
            elif(piecePlayer1.row+piecePlayer1.col>=14):
                player1PiecesInPlayer2House = player1PiecesInPlayer2House+1
            #Check pieces player 2 count
            if(piecePlayer2.row+piecePlayer2.col<=4):
                player2PiecesInPlayer1House = player2PiecesInPlayer1House+1
            elif(piecePlayer2.row+piecePlayer2.col>=14):
                player2PiecesInPlayer2House = player2PiecesInPlayer2House+1
        #Check to see if someone has won
        if(player1PiecesInPlayer2House+player2PiecesInPlayer2House==15 and player1PiecesInPlayer2House>=1):
            return PLAYER_1_COLOR
        elif(player1PiecesInPlayer1House+player2PiecesInPlayer1House==15 and player2PiecesInPlayer1House>=1):
            return PLAYER_2_COLOR
        return False

    def isTerminal(self):
        player1PiecesInPlayer2House = 0
        player2PiecesInPlayer1House = 0
        player1PiecesInPlayer1House = 0
        player2PiecesInPlayer2House = 0
        for i in range(len(self.board.piecesPlayer1)):
            piecePlayer1 = self.board.piecesPlayer1[i]
            piecePlayer2 = self.board.piecesPlayer2[i]
            #Check pieces player 1 count
            if(piecePlayer1.row+piecePlayer1.col<=4):
                player1PiecesInPlayer1House = player1PiecesInPlayer1House+1
            elif(piecePlayer1.row+piecePlayer1.col>=14):
                player1PiecesInPlayer2House = player1PiecesInPlayer2House+1
            #Check pieces player 2 count
            if(piecePlayer2.row+piecePlayer2.col<=4):
                player2PiecesInPlayer1House = player2PiecesInPlayer1House+1
            elif(piecePlayer2.row+piecePlayer2.col>=14):
                player2PiecesInPlayer2House = player2PiecesInPlayer2House+1
        #Check to see if someone has won
        if(player1PiecesInPlayer2House+player2PiecesInPlayer2House==12 and player1PiecesInPlayer2House>=1):

            return PLAYER_1_COLOR
        elif(player1PiecesInPlayer1House+player2PiecesInPlayer1House==12 and player2PiecesInPlayer1House>=1):

            return PLAYER_2_COLOR
        return False

