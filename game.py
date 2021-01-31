# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# Hoppers game.py

from board import Board
from game_options import PLAYER_1_COLOR,PLAYER_2_COLOR

class Game:
    def __init__(self,display):
        self.display = display
        self.board = Board(display)
        self.turn = PLAYER_1_COLOR
        self.selectedPiece = 0
        self.possibleMoves = []
        self.possibleDestinations = []

    def move(self,fromRow,fromCol,row,col):
        self.board.move(fromRow,fromCol,row,col)
        self.selectedPiece = 0
        self.changeTurn()

    # def getPathToDestinations(self,fromRow,fromCol,row,col):
    #     self.board.move(fromRow,fromCol,row,col)
    #     self.selectedPiece = 0
    #     self.changeTurn()

    def selectPiece(self,row,col):
        self.selectedPiece = self.board.getPiece(row,col)
        self.board.draw_board()
        if(self.selectedPiece!=0 and self.selectedPiece.color==self.turn):
            self.possibleDestinations,self.possibleMoves=self.board.drawPossibleMoves(self.selectedPiece)
            hola=5
        else:
            self.selectedPiece =0

    def changeTurn(self):
        if self.turn==PLAYER_1_COLOR:
            self.turn=PLAYER_2_COLOR
        else:
            self.turn=PLAYER_1_COLOR

    def checkWin():
        return False