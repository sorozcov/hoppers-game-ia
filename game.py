# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# Hoppers game.py

from board import Board
from game_options import PLAYER_1_COLOR,PLAYER_2_COLOR
import copy
import pygame
import pandas
import itertools
import time

#Class Game Hoppers
class Game:
    def __init__(self,display=None):
        self.board = Board(display)
        self.turn = PLAYER_1_COLOR
        self.selectedPiece = 0
        self.possibleMoves = []
        self.possibleDestinations = []

    #Deep copy of self
    def copy(self):
        return copy.deepcopy(self)

    #Move given coordinates of board
    #Display if using pygame display
    def move(self,fromRow,fromCol,row,col,display=None):
        self.board.move(fromRow,fromCol,row,col,display)
        self.selectedPiece = 0
        self.changeTurn()
        return self.copy()

    #Move from given move action
    #Display if using pygame display
    def moveAction(self,action,printPath=False,display=None):
        initSpace= action.fullPath[0]
        endSpace = action
        self.board.move(initSpace[0],initSpace[1],endSpace.currentRow,endSpace.currentCol,display)
        self.selectedPiece = 0
        self.changeTurn()
        return self.copy()
    
    #Move action step by step on pygame display
    def moveActionStepByStep(self,action,printPath=False,display=None):

        for indexStep in range(len(action.fullPath)-1):
            initSpace = action.fullPath[indexStep]
            endSpace = action.fullPath[indexStep+1]

            piece = self.board.board[initSpace[0]][initSpace[1]]
            piece.drawSelected(display)
            pygame.display.update()
            time.sleep(2)
            self.board.move(initSpace[0],initSpace[1],endSpace[0],endSpace[1],display)
            pygame.display.update()
            self.selectedPiece = 0
        self.changeTurn()
        return self.copy()
    
    #Move Action and return a copy
    #This is a hypothetical move in a new board
    def moveActionCopy(self,action,printPath=False,display=None):
        gameCopy = self.copy()
        initSpace= action.fullPath[0]
        endSpace = action
        gameCopy.move(initSpace[0],initSpace[1],endSpace.currentRow,endSpace.currentCol,display)
        gameCopy.selectedPiece = 0
        gameCopy.changeTurn()
        return gameCopy

    #Check list of a possible moves
    def checkPossibleMoves(self,omitPiecesInPositions=[]):
        pieces = self.board.piecesPlayer1 if self.turn==PLAYER_1_COLOR else self.board.piecesPlayer2
        # moves = list(itertools.chain.from_iterable(map(self.checkPossibleMovesPiece,pieces,omitPiecesInPositions)))
        moves =[]
        [moves.extend(self.checkPossibleMovesPiece(piece,omitPiecesInPositions)) for piece in pieces]  
        # moves.sort(key=lambda move: len(move.fullPath) ,reverse=True)
        moves.sort(key=lambda move: self.calculateDistance(move,self.turn==PLAYER_1_COLOR) ,reverse=True)
        return moves
    
    # Function to sort moves
    def calculateDistance(self,move,player1=True):
        init = move.fullPath[0]
        distance = ((move.currentRow-init[0])**2 + (move.currentCol - init[1])**2)**(1/2)
        try:
            m = (move.currentRow-init[0])/(move.currentCol - init[1])
        except:
            m=1
        sign = +1 if m>0 else (-1 if m<0 else 0)
        if(player1):
            return sign*distance
        else:
            return sign*distance

    #Check possibles moves given a piece of game
    def checkPossibleMovesPiece(self,piece,omitPiecesInPositions=[]):
        return  [] if (piece.row,piece.col) in omitPiecesInPositions else piece.possibleMoves(self.board)

    # Return the turn of player
    def toMoveTurn(self):
        return self.turn


    # Select a piece to move it and show its possible moves
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

    #Change players turn
    def changeTurn(self):
        if self.turn==PLAYER_1_COLOR:
            self.turn=PLAYER_2_COLOR
        else:
            self.turn=PLAYER_1_COLOR

    #Check if win on game
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

    #Check if is terminal node and if someone won
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

